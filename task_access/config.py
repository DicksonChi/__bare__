from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from constants import DB_DIR

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_DIR
DB = SQLAlchemy(app)
