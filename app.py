from flask import Flask
# from flask_wtf.csrf import CSRFProtect    # This is for the CSRF protection

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# FLAW 1
# This is the CSRF protection
# csrf = CSRFProtect(app)
