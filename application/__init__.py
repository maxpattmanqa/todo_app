from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.197.197.56/todo_db"
app.config["SECRET_KEY"] = "secret_key"

db = SQLAlchemy(app)

from application import routes