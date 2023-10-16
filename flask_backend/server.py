from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from flask_marshmallow import Marshmallow
import models
from markupsafe import escape

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # SQLite database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/test2")
def index():
    result = models.session.execute(select(models.User))

    test = []
    for user_obj in result.scalars():
        test.append(user_obj.name)

    print(test)

    # return ["test1", "test2", "test3"]
    return jsonify(test)


@app.route("/test")
def test():
    # return {"test"}
    return ["test1", "test2", "test3"]


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


class TodoSchema(ma.Schema):
    class Meta:
        fields = ("todo_id", "todo_text", "todo_date")


todo_schema = TodoSchema()


@app.route("/get/todos", methods=["GET"])
def get_todos():
    all_todos = models.session.execute(select(models.Todo))

    result = []
    for user_obj in all_todos.scalars():
        result.append(todo_schema.dump(user_obj))

    return jsonify(result)


@app.route("/add/todo", methods=["POST"])
def add_todo():
    todo_text = request.json["todo_text"]

    todo = models.Todo(todo_text)
    models.session.add(todo)
    models.session.commit()
    return todo_schema.jsonify(todo)


@app.route("/delete/todo/<id>", methods=["GET"])
def delete_todo(id):
    query = models.session.get(models.Todo, id)

    result = []
    result.append(query.todo_text)
    models.session.delete(query)
    models.session.commit()

    return jsonify("deleted")


@app.route("/delete/users")
def delete_users():
    query = models.session.execute(select(models.User))

    for user_obj in query.scalars():
        models.session.delete(user_obj)

    return jsonify("users deleted")


@app.route("/users")
def get_users():
    query = models.session.execute(select(models.User))

    users = []
    for user_obj in query.scalars():
        users.append(user_obj.name)

    return jsonify(users)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
