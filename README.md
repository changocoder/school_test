# School App
Flask, Flask-Login, Login with Google, App setup as Google Client

Installation with Poetry:
```bash
poetry install
```

Run the app:
```bash
poetry run python app.py
```

# Google Client Setup
1. Go to https://console.developers.google.com/
2. Create a new project
3. Go to Credentials
4. Create credentials
5. OAuth client ID
6. Application type: Web application
7. Authorized JavaScript origins: http://localhost:5000
8. Authorized redirect URIs: http://localhost:5000/login/callback
9. Create
10. Copy the client ID and client secret to the .env file
11. Add the client ID and client secret to the GoogleLogin class in app.py
12. Run the app
13. Go to http://localhost:5000/login
14. Login with Google
15. You should see your email and profile picture
16. Logout