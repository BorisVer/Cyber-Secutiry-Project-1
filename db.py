from flask_sqlalchemy import SQLAlchemy
from app import app

# Configure the database URI; this creates a file named "mydatabase.db" in your project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/boris/Documents/CyberSecurity/project/mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
