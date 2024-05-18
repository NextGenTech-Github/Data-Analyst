import os
import json
import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'a_secret_key')  # Replace with your actual secret key
# Get the current working directory
current_dir = os.getcwd()

# OAuth configuration
oauth = OAuth(app)
oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_access_token_params=None,
    authorize_redirect_uri='http://localhost:5000/auth',
    client_kwargs={'scope': 'openid email profile'}
)

# Load responses from JSON file
with open(current_dir + '/ChatBot/responses.json', 'r') as file:
    responses = json.load(file)

def get_response(user_input):
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

@app.route("/")
def home():
    user = session.get('user')
    return render_template("index.html", user=user)

@app.route("/login")
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/auth")
def auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session['user'] = user
    return redirect('/')

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json["msg"]
    response_text = get_response(user_input)
    return jsonify({"response": response_text})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)
