from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import models
from markupsafe import escape

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # SQLite database
db = SQLAlchemy(app)


@app.route("/test2")
def index():
    result = models.session.execute(select(models.User))

    test = []
    for user_obj in result.scalars():
        test.append(user_obj.name)

    return jsonify(test)


@app.route("/test")
def test():
    # return {"test"}
    return {"test": ["test1", "test2", "test3"]}


@app.route("/add/<username>")
def add_user(username):
    name = f"{escape(username)}"
    models.session.add(models.User(6, f"{escape(username)}"))
    models.session.commit()
    return name


@app.route("/test3")
def add_test():
    user1 = models.User(1, "dude")
    user2 = models.User(2, "sponge bob")
    user3 = models.User(3, "patrick")
    user4 = models.User(4, "mr crabs")
    user5 = models.User(5, "sandy")
    models.session.add(user1)
    models.session.add(user2)
    models.session.add(user3)
    models.session.add(user4)
    models.session.add(user5)
    models.session.commit()
    return "adding data"


if __name__ == "__main__":
    app.run(port=8000, debug=True)
