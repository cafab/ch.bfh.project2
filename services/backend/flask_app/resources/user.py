"""from flask_restful import Resource, reqparse
from flask_app.models.user import UserModel


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
        return "Hello User from private endpoint yolo!"""""
