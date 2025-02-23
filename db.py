from flask_sqlalchemy import SQLAlchemy
from app import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print("To simulate the CSRF attack use: " + basedir + "/templates/csrf_attack.html")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
