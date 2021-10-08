"""
application
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


class Todo(db.Model): # pylint: disable=too-few-public-methods
    """A dummy docstring."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@application.route("/edit")
def home1():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@application.route("/")
def list1():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)


@application.route("/add", methods=["POST"])
def add():
    """A dummy docstring."""
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home1"))


@application.route("/update/<int:todo_id>")
def update(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home1"))


@application.route("/delete/<int:todo_id>")
def delete(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home1"))


if __name__ == "__main__":
    db.create_all()
    application.run(host='0.0.0.0',port=8080,debug=True)
