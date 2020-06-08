# Project 2 - Technology-Study Auth0

This Project is about figuring out a suitable authentication and authorization method for building a Bitcoin Trading Bot website, where users can sign up and safely store
their exchange apy-keys.

## Technologies

Following technologies have been used:

- [**Flask**](https://palletsprojects.com/p/flask/) *as a Python REST-API resource server backend.*
- [**Vue.js**](https://vuejs.org/) *as a Javascript SPA client frontend.*
- [**PostgreSQL**](https://www.postgresql.org/) *as a relational database for storing sensitive information about the user.*
- [**Docker**](https://www.docker.com/) *in order to isolate and virtualize each application component above in a container.*

## How I did it

The requirements for the architecture of this project were given by my coach Kai Brünnler. The idea was to have a mechanism to authenticate a user through an identity provider and give him access to a resource server which handles authorized API requests. The main focus therefore was on the security aspect of the authentication and authorization process.

We chose [**Auth0**](https://auth0.com/) as a third-party identity provider and authorization server. Auth0 uses [**OpenID Connect (OIDC)**](https://openid.net/connect/) and [**OAuth 2.0**](https://tools.ietf.org/html/rfc6749) to authenticate users and get their authorization to access protected resources.

Additionally, we decided to use the lightweight and in popularity gaining Javascript framework Vue.js as the frontend client and likewise a lightweight backend web framework for which we chose Flask.

At the start of the project I had to familiarize with these technologies so I did following tutorials both provided by Auth0:

- [**Vue.js with User Login**](https://auth0.com/blog/beginner-vuejs-tutorial-with-user-login/)

- [**Python API: Authorization**](https://auth0.com/docs/quickstart/backend/python/01-authorization)

Furthermore I had to freshen up the various authentication and authorization flows for the respective applications and APIs. I found out that in order to ensure a public client like the Vue.js app is doesn't leak the client secret, I have to pick the Authorization Code Flow with Proof Key for Code Exchange (PKCE). Check out my presentation [**here**](docs/Auth_Code_Flow_with_PKCE.odp) of why we have to use this kind of flow and what attacks would be possible if we wouldn't. Luckily, Auth0 provides us with a suitable [**SDK**](https://auth0.com/docs/libraries/auth0-spa-js) for this flow.

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

5. &nbsp;Still connected to the database (see 1.), run &nbsp;`\dt`. Now the "users" table has been created. If you enter the command &nbsp;`select * from users;`&nbsp; you will see an entry of the &nbsp;`jodod47804@gilfun.com`&nbsp; with the user_id extracted from the access token "sub" claim.
