# Project 2

This Project is about figuring out a suitable authentication and authorization method for building a Bitcoin Trading Bot website, where users can sign up and safely store
their exchange API keys.

## Technologies

Following technologies have been used:

- [**Flask**](https://palletsprojects.com/p/flask/) *as a REST-API resource server backend.*
- [**Vue.js**](https://vuejs.org/) *as a SPA client frontend.*
- [**PostgreSQL**](https://www.postgresql.org/) *as a relational database for storing sensitive information about the user.*
- [**Docker**](https://www.docker.com/) *to isolate and virtualize each application in a container.*

## Authentication and Authorization

To handle authentication and authorize users to access the project's resource server (Flask backend), this project makes use of [**Auth0**](https://auth0.com/) as an identity provider and authorization server. Auth0 uses the [**OAuth2**](https://tools.ietf.org/html/rfc6749) protocol for authorization and [**OpenID Connect**](https://openid.net/connect/) as an authentication layer on top of OAuth2.

## API Calls

When public clients (e.g., native and single-page applications) request Access Tokens, some additional security concerns are posed that are not mitigated by the Authorization Code Flow alone. Our Vue.js client cannot securely store the client secret because the entire source is available to the browser. Client secrets prove to an authentication server, that a client app is authorized to make requests on behalf of a user. Therefore this project fits best for the [**Authorization Code Flow with Proof Key for Code Exchange (PKCE)**](https://tools.ietf.org/html/rfc7636), where our Vue.js client exchanges a challenge with the Auth0 authorization server in order to get a valid access and id token. Luckily, Auth0 provides us with a suitable [**SDK**](https://auth0.com/docs/libraries/auth0-spa-js) for this matter.

## Installation guide

Prerequisites: Make sure you have [**Docker**](https://docs.docker.com/get-docker/) and [**Docker-Compose**](https://docs.docker.com/compose/install/) installed.

1. &nbsp;Clone this project to your computer.

2. &nbsp;`cd`&nbsp; into the project folder.

3. &nbsp;Run &nbsp;`docker-compose up -d --build`&nbsp; to set up and start the docker containers.

4. &nbsp;Run &nbsp;`docker ps`&nbsp; to see the running containers and their ports.

5. Open your favourite browser and enter &nbsp;`http://localhost:3000`&nbsp; in the address bar in order to call the Vue app.

## Test the app

1. &nbsp;First, have a look at our initialized postgres database by running the following command in the project root folder: &nbsp;`docker-compose exec db psql --username=project2 --dbname=project2db`. You are now connected to the "project2db" database. Then run &nbsp;`\dt`. You see that there are no relations (tables) defined.

2. &nbsp;Now go again to the Vue app and click "Sign in" using the test email &nbsp;`jodod47804@gilfun.com`&nbsp; and the password &nbsp;`Projekt2!`. After the successful login you'll be redirected from Auth0 to our app with a valid access and id token in memory.

3. &nbsp;You may notice that the navigation bar element "Dashboard" appeared at the top, meaning we are authenticated and can access our personal dashboard.

4. &nbsp;Now when you click on "Dashboard", the access token along with the extracted email address from the id token will for the first time be sent to our Flask backend.  

The backend will then validate our access token by checking the token signature against the corresponding public key from Auth0. When the validation succeeded, the subject information from the access token gets extracted, which uniquely identifies the user. This user id will then be stored in the postgres database along with the email address already extraced from the id token in the Vue client app. Id tokens shall never be used to get access to an API. Id tokens are the OpenId Connect part in the authentication flow and are meant to leverage user experience by showing user specific data on the client side like first and last name of the user for example.

This app isn't complete yet, because the focus of this project was on the authentication and authorization part of users to make API calls to our backend so they can store sensitive data like an exchange api-key in our own database without having to outsource this information to Auth0, which would also have been possible but would be out of our control of how they treat this data.
