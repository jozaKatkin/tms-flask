import os
from flask import Flask
from hw18.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
app.config.update(SECRET_KEY=os.urandom(24))

db = SQLAlchemy(app)
