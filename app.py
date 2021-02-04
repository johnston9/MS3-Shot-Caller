import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.register_key = os.environ.get("REGISTER_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check db for matching username
        old_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if old_user:
            # use Wertzeug to check stored password matches user input
            if check_password_hash(
                old_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hi {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "user_home", username=session["user"]))
            else:
                # invalid password match
                flash("Entry Incorrect")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Entry Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.form.get("key").lower() == app.register_key:

            # check to see if username is taken
            old_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if old_user:
                flash("Username taken try again")
                return redirect(url_for("register"))

            new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(new_user)

            # set session cookie to this username
            session["user"] = request.form.get("username").lower()
            flash("Welcome aboard")
            return redirect(url_for("user_home", username=session["user"]))
        else:
            flash("invalid key")
    return render_template("register.html")


@app.route("/user_home/<username>", methods=["GET", "POST"])
def user_home(username):
    # make sure session user's username exists in db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("user_home.html", username=username)


@app.route("/get_depts")
def get_depts():
    depts = mongo.db.depts.find()
    return render_template("depts.html", depts=depts)


@app.route("/get_camera")
def get_camera():
    camera = mongo.db.camera_dept.find()
    return render_template("camera.html", camera=camera)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
