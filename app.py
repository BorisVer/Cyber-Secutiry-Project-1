from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change to a secure key in production
