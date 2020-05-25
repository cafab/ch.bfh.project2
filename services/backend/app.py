
from flask import Flask, jsonify, request, _request_ctx_stack
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from functools import wraps
from six.moves.urllib.request import urlopen
from jose import jwt
import json

from flask_app.models.user import UserModel

app = Flask(__name__)
app.config.from_object("flask_app.config.Config")
api = Api(app)
CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization"])



AUTH0_DOMAIN = app.config['AUTH0_DOMAIN']
API_IDENTIFIER = app.config['API_IDENTIFIER']
ALGORITHMS = app.config['ALGORITHMS']


# Format error response and append status code.
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return True
    return False


def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_IDENTIFIER,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated


def get_user_id_from_token():
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("sub"):
        return unverified_claims.get("sub")


class Resource(Resource):
    method_decorators = [requires_auth]


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")


    def post(self):
        data = User.parser.parse_args()
        user_id = get_user_id_from_token()
        # If there isn't a user with this email in the database, create one.
        if not UserModel.find_by_id(user_id):
            user = UserModel(user_id=user_id, email=data['email'], first_name='', last_name='')
            user.save_to_db()
            return {"message": "User {} created successfully!".format(user.email)}, 201
        return {"error": "User already exists!"}

    def get(self):
        return "Hello User from private endpoint yolo!"


@app.before_first_request
def create_tables():
    db.create_all()
    print("create_tables")


api.add_resource(User, '/api/user')

if __name__ == '__main__':
    from flask_app.db import db
    db.init_app(app)
    print("main")
    app.run(host='0.0.0.0')






