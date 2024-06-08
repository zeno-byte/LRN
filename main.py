from flask import Flask, request
import requests

app = Flask(__name__)

# Replace these with your actual LinkedIn app credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'https://yourusername.github.io/linkedin-auth-redirect'

@app.route('/')
def home():
    return 'Welcome to the LinkedIn OAuth handler'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get('access_token')
    return f'Access Token: {access_token}'

if __name__ == '__main__':
    app.run(debug=True)

