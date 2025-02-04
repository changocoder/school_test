# import requests
# from flask import json
# from flask import redirect
# from flask import request
# from flask import url_for
# from flask_login import current_user
# from flask_login import login_manager
# from flask_login import login_required
# from flask_login import login_user
# from flask_login import logout_user
#
# from app.config import ConfigClass
# from app.models.user import User
# from app.runner import app
# from app.runner import client
# from app.services.user import UserService
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return UserService.get_by_id(user_id)
#
#
# @app.route("/")
# def index():
#     if current_user.is_authenticated:
#         return (
#             "<p>Hello, {}! You're logged in! Email: {}</p>"
#             "<div><p>Google Profile Picture:</p>"
#             '<img src="{}" alt="Google profile pic"></img></div>'
#             '<a class="button" href="/logout">Logout</a>'.format(
#                 current_user.name, current_user.email, current_user.profile_pic
#             )
#         )
#     else:
#         return '<a class="button" href="/login">Google Login</a>'
#
#
# @app.route("/login")
# def login():
#     # Find out what URL to hit for Google login
#     google_provider_cfg = get_google_provider_cfg()
#     authorization_endpoint = google_provider_cfg["authorization_endpoint"]
#
#     # Use library to construct the request for login and provide
#     # scopes that let you retrieve user's profile from Google
#     request_uri = client.prepare_request_uri(
#         authorization_endpoint,
#         redirect_uri=request.base_url + "/callback",
#         scope=["openid", "email", "profile"],
#     )
#     return redirect(request_uri)
#
#
# @app.route("/login/callback")
# def callback():
#     # Get authorization code Google sent back to you
#     code = request.args.get("code")
#
#     # Find out what URL to hit to get tokens that allow you to ask for
#     # things on behalf of a user
#     google_provider_cfg = get_google_provider_cfg()
#     token_endpoint = google_provider_cfg["token_endpoint"]
#
#     # Prepare and send request to get tokens! Yay tokens!
#     token_url, headers, body = client.prepare_token_request(
#         token_endpoint,
#         authorization_response=request.url,
#         redirect_url=request.base_url,
#         code=code,
#     )
#     token_response = requests.post(
#         token_url,
#         headers=headers,
#         data=body,
#         auth=(ConfigClass.GOOGLE_CLIENT_ID, ConfigClass.GOOGLE_CLIENT_SECRET),
#     )
#
#     # Parse the tokens!
#     client.parse_request_body_response(json.dumps(token_response.json()))
#
#     # Now that we have tokens (yay) let's find and hit URL
#     # from Google that gives you user's profile information,
#     # including their Google Profile Image and Email
#     userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
#     uri, headers, body = client.add_token(userinfo_endpoint)
#     userinfo_response = requests.get(uri, headers=headers, data=body)
#
#     # We want to make sure their email is verified.
#     # The user authenticated with Google, authorized our
#     # app, and now we've verified their email through Google!
#     if userinfo_response.json().get("email_verified"):
#         unique_id = userinfo_response.json()["sub"]
#         users_email = userinfo_response.json()["email"]
#         picture = userinfo_response.json()["picture"]
#         users_name = userinfo_response.json()["given_name"]
#     else:
#         return "User email not available or not verified by Google.", 400
#
#     # Create a user in our db with the information provided
#     # by Google
#     user = User(id_=unique_id, name=users_name, email=users_email, profile_pic=picture)
#
#     # Doesn't exist? Add to database
#     if not User.get(unique_id):
#         User.create(unique_id, users_name, users_email, picture)
#
#     # Begin user session by logging the user in
#     login_user(user)
#
#     # Send user back to homepage
#     return redirect(url_for("index"))
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("index"))
#
#
# def get_google_provider_cfg():
#     return requests.get(GOOGLE_DISCOVERY_URL).json()
