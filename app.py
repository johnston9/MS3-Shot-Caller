import os
import datetime
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
                "firstname": request.form.get("firstname").lower(),
                "lastname": request.form.get("lastname").lower(),
                "job_title": request.form.get("job_title"),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(new_user)

            # set session cookie to this username
            session["user"] = request.form.get("username").lower()
            flash("Welcome aboard, {}".format(
                            request.form.get("username")))
            return redirect(url_for("user_home", username=session["user"]))
        else:
            flash("invalid key")
    return render_template("register.html")


@app.route("/user_home/<username>", methods=["GET", "POST"])
def user_home(username):
    script = list(mongo.db.latest_script.find())
    depts = list(mongo.db.depts.find())
    shotlist = list(mongo.db.shotlist.find())
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template(
            "user_home.html", username=username,
            script=script, shotlist=shotlist, depts=depts)

    return redirect(url_for("login"))

 
@app.route("/get_depts")
def get_depts():
    depts = mongo.db.depts.find()
    return render_template("depts.html", depts=depts)


@app.route("/get_dep/<dep>", methods=["GET", "POST"])
def get_dep(dep):
    dep = dep
    depart = list(mongo.db[dep].find())
    day = datetime.datetime.now()
    today = day.strftime("%d %B, %Y")
    if request.method == "POST":
        date = request.form.get("date")
        print(date)
        return render_template(
            "dep.html", dep=dep, depart=depart, date=date, day=date)
    return render_template(
        "dep.html", dep=dep, depart=depart, date=today, day="TODAY")


@app.route("/get_poster/<dep>", methods=["GET", "POST"])
def get_poster(dep):
    dep = dep
    if request.method == "POST":
        x = request.form.get("poster").lower()
        depart = list(mongo.db[dep].find(
            {"poster": x}))

        return render_template(
            "dep-poster.html", dep=dep, depart=depart)
    return render_template(
        "dep-poster.html", dep=dep)


@app.route("/get_all/<dep>", methods=["GET", "POST"])
def get_all(dep):
    dep = dep
    depart = list(mongo.db[dep].find())

    return render_template(
            "dep-poster.html", dep=dep, depart=depart)


@app.route("/get_image/", methods=["GET", "POST"])
def get_image():
    if request.method == "POST":
        image = request.form.get("image")
        images = list(mongo.db.images.find({"$text": {"$search": image}}))
        return render_template("images.html", images=images)

    images = list(mongo.db.images.find({"image_name": "cat"}))
    return render_template("images.html", images=images)


@app.route("/logout")
def logout():
    # delete user session cookie
    flash("Logout successful")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_message", methods=["GET", "POST"])
def add_message():
    if request.method == "POST":
        mes_is_priority = "on" if request.form.get("is_priority") else "off"
        day = datetime.datetime.now()
        mes_date = day.strftime("%d %B, %Y")
        mes_dept = request.form.get("department_name")
        user = mongo.db.users.find_one({"username": session["user"]})
        first = user["firstname"]
        last = user["lastname"]
        username = session["user"]
        mes_poster = f"{first} {last}"
        mes_job = user["job_title"]
        message = {
            "dept_name": mes_dept,
            "date": mes_date,
            "poster": mes_poster,
            "username": username,
            "job_title": mes_job,
            "subject": request.form.get("subject"),
            "message": request.form.get("message"),
            "image_src": request.form.get("image_src"),
            "image_des": request.form.get("image_des"),
            "is_priority": mes_is_priority,
        }
        mongo.db[mes_dept].insert_one(message)
        flash("Message Added")
        return redirect(url_for("user_home", username=session["user"]))

    depts = mongo.db.depts.find().sort("dept_name", 1)
    return render_template("add_message.html", depts=depts)


@app.route("/edit_message/<message_id>/<depart>", methods=["GET", "POST"])
def edit_message(message_id, depart):
    if request.method == "POST":
        mes_is_priority = "on" if request.form.get("is_priority") else "off"
        day = datetime.datetime.now()
        mes_date = day.strftime("%d %B, %Y")
        mes_dept = request.form.get("department_name")
        user = mongo.db.users.find_one({"username": session["user"]})
        first = user["firstname"]
        last = user["lastname"]
        mes_poster = f"{first} {last}"
        mes_job = user["job_title"]
        edit = {
            "dept_name": mes_dept,
            "date": mes_date,
            "poster": mes_poster,
            "job_title": mes_job,
            "subject": request.form.get("subject"),
            "message": request.form.get("message"),
            "image_src": request.form.get("image_src"),
            "image_des": request.form.get("image_des"),
            "is_priority": mes_is_priority,
        }
        mongo.db[mes_dept].update({"_id": ObjectId(message_id)}, edit)
        flash("Message Updated")
        return redirect(url_for("get_dep", dep=mes_dept))

    message = mongo.db[depart].find_one({"_id": ObjectId(message_id)})
    depts = mongo.db.depts.find().sort("dept_name", 1)
    return render_template("edit_message.html", message=message, depts=depts)


@app.route("/delete_message/<message_id>/<depart>")
def delete_message(message_id, depart):
    mongo.db[depart].remove({"_id": ObjectId(message_id)})
    flash("Message Deleted")
    return redirect(url_for("get_dep", dep=depart))


@app.route("/add_script/<script_id>", methods=["GET", "POST"])
def add_script(script_id):
    script = list(mongo.db.latest_script.find())
    if request.method == "POST":
        latest = {
            "script": request.form.get("script_name")
        }
        mongo.db.latest_script.update(
            {"_id": ObjectId(script_id)}, latest)
        flash("Script Successfully Updated")
        return redirect(url_for("user_home", username=session["user"]))

    return render_template("add_script.html", script=script)


@app.route("/add_shot", methods=["GET", "POST"])
def add_shot():
    if request.method == "POST":
        newshot = {
            "shotlist": request.form.get("shot_name")
        }
        mongo.db.shotlist.update(
            {"_id": ObjectId("6029b7f80febec6e0f942fcb")}, newshot)
        flash("Shotlist Successfully Updated")
        return redirect(url_for("user_home", username=session["user"]))

    return render_template("add_shotlist.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
