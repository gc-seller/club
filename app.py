import json
import base64
import warnings
from flask import Flask, redirect, url_for, session, request, render_template, flash
from pymongo import MongoClient
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText



app = Flask(__name__)
app.secret_key = "supersecretkey"  # replace with a strong random key in production

@app.route('/')
def index():
    return render_template('index.html', creds_saved=True)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
