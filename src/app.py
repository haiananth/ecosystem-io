from flask import Flask, render_template, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
from os import environ
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get('FLASK_SECRET_KEY')

oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=environ.get('AUTH0_CLIENT_ID'),
    client_secret=environ.get('AUTH0_CLIENT_SECRET'),
    api_base_url=f'https://{environ.get("AUTH0_DOMAIN")}',
    access_token_url=f'https://{environ.get("AUTH0_DOMAIN")}/oauth/token',
    authorize_url=f'https://{environ.get("AUTH0_DOMAIN")}/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f'https://{environ.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route('/')
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

@app.route('/login')
def login():
    return auth0.authorize_redirect(
        redirect_uri=url_for('callback', _external=True),
        audience=environ.get('API_IDENTIFIER')
    )

@app.route('/callback')
def callback():
    try:
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()
        session['user'] = userinfo
        return redirect(url_for('dashboard'))
    except Exception as e:
        print(f"Error in callback: {str(e)}")
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(
        f'https://{environ.get("AUTH0_DOMAIN")}/v2/logout?'
        f'client_id={environ.get("AUTH0_CLIENT_ID")}&'
        f'returnTo={url_for("home", _external=True)}'
    )

if __name__ == '__main__':
    app.run(debug=True, port=3000)