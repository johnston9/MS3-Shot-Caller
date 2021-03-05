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
            if check_password_hash(old_user["password"], request.form.get(
                    "password")):
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
                "job_title": request.form.get("job_title").title(),
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
    if session["user"]:
        script = list(mongo.db.latest_script.find())
        depts = list(mongo.db.depts.find())
        shotlist = list(mongo.db.shotlist.find())
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template(
            "user_home.html", username=username,
            script=script, shotlist=shotlist, depts=depts)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/get_depts")
def get_depts():
    if session["user"]:
        depts = mongo.db.depts.find()
        return render_template("depts.html", depts=depts)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/get_pro")
def get_pro():
    if session["user"]:
        day = datetime.datetime.now()
        today = day.strftime("%d %B, %Y")
        depart = list(mongo.db.production.find({"date": today}))

        return render_template(
            "pro.html", dep="Today's Production Updates", depart=depart,
            date=today, day="TODAY")


@app.route("/get_dep/<dep>", methods=["GET", "POST"])
def get_dep(dep):
    if session["user"]:
        dep = dep
        day = datetime.datetime.now()
        today = day.strftime("%d %B, %Y")
        depart = list(mongo.db[dep].find({"date": today}))
        if request.method == "POST":
            date = request.form.get("date")
            depart = list(mongo.db[dep].find(
                {"date": date}))

            return render_template(
                "dep.html", dep=dep, depart=depart, date=date, day=date)
        return render_template(
            "dep.html", dep=dep, depart=depart, date=today, day="TODAY")

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/get_poster/<dep>", methods=["GET", "POST"])
def get_poster(dep):
    if session["user"]:
        dep = dep
        if request.method == "POST":
            poster = request.form.get("poster").lower()
            depart = list(mongo.db[dep].find(
                {"poster": poster}))

            return render_template(
                "dep-poster.html", dep=dep, depart=depart, day=poster)
        return render_template(
            "dep-poster.html", dep=dep)
    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/get_all/<dep>", methods=["GET", "POST"])
def get_all(dep):
    if session["user"]:
        dep = dep
        depart = list(mongo.db[dep].find())

        return render_template(
            "dep.html", dep=dep, depart=depart, day="All Messages")
    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/find_all/<dep>", methods=["GET", "POST"])
def find_all(dep):
    if session["user"]:
        dep = dep
        depart = list(mongo.db[dep].find())

        return render_template(
            "dep-poster.html", dep=dep, depart=depart, day="All Messages")

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/all_images/", methods=["GET", "POST"])
def all_images():
    if session["user"]:
        images = list(mongo.db.images.find())
        return render_template("images.html", images=images)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/get_image/", methods=["GET", "POST"])
def get_image():
    if session["user"]:
        if request.method == "POST":
            image = request.form.get("image")
            images = list(mongo.db.images.find({"$text": {"$search": image}}))
            return render_template("images.html", images=images)

        images = list(mongo.db.images.find({"image_name": "windowlight"}))
        return render_template("images.html", images=images)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if session["user"]:
        # delete user session cookie
        flash("Logout successful")
        session.pop("user")
        return redirect(url_for("login"))


@app.route("/add_message", methods=["GET", "POST"])
def add_message():
    if session["user"]:
        if request.method == "POST":
            mes_is_priority = "on" if request.form.get(
                "is_priority") else "off"
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
                "image_name": request.form.get("image_name"),
                "is_priority": mes_is_priority,
            }
            mongo.db[mes_dept].insert_one(message)
            flash("Message Added")
            return redirect(url_for("user_home", username=session["user"]))

        depts = mongo.db.depts.find().sort("dept_name", 1)
        return render_template("add_message.html", depts=depts)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route(
    "/edit_message/<message_id>/<depart>/<user>", methods=["GET", "POST"])
def edit_message(message_id, depart, user):
    if session["user"] == user:
        if request.method == "POST":
            mes_is_priority = "on" if request.form.get(
                "is_priority") else "off"
            day = datetime.datetime.now()
            mes_date = day.strftime("%d %B, %Y")
            mes_dept = request.form.get("department_name")
            user = mongo.db.users.find_one({"username": session["user"]})
            username = session["user"]
            first = user["firstname"]
            last = user["lastname"]
            mes_poster = f"{first} {last}"
            mes_job = user["job_title"]
            edit = {
                "dept_name": mes_dept,
                "date": mes_date,
                "poster": mes_poster,
                "username": username,
                "job_title": mes_job,
                "subject": request.form.get("subject"),
                "message": request.form.get("message"),
                "image_src": request.form.get("image_src"),
                "image_name": request.form.get("image_name"),
                "is_priority": mes_is_priority,
            }
            mongo.db[mes_dept].update({"_id": ObjectId(message_id)}, edit)
            flash("Message Updated")
            return redirect(url_for("get_dep", dep=mes_dept))

        message = mongo.db[depart].find_one({"_id": ObjectId(message_id)})
        depts = mongo.db.depts.find().sort("dept_name", 1)
        return render_template(
            "edit_message.html", message=message, depts=depts)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/edit_image/<image_id>", methods=["GET", "POST"])
def edit_image(image_id):
    if session["user"] == "admin":
        if request.method == "POST":
            edit = {
                "image_name": request.form.get("image_name"),
                "image_des": request.form.get("image_des"),
                "image_src": request.form.get("image_src")
            }
            mongo.db.images.update({"_id": ObjectId(image_id)}, edit)
            flash("Image Updated")
            return redirect(url_for("get_image"))

        image = mongo.db.images.find_one({"_id": ObjectId(image_id)})
        return render_template("edit_image.html", image=image)

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/delete_message/<message_id>/<depart>/<user>")
def delete_message(message_id, depart, user):
    if session["user"] == user:
        mongo.db[depart].remove({"_id": ObjectId(message_id)})
        flash("Message Deleted")
        return redirect(url_for("get_dep", dep=depart))

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/add_script/<script_id>", methods=["GET", "POST"])
def add_script(script_id):
    if session["user"] == "admin":
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

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/add_shot", methods=["GET", "POST"])
def add_shot():
    if session["user"] == "admin":
        if request.method == "POST":
            newshot = {
                "shotlist": request.form.get("shot_name")
            }
            mongo.db.shotlist.update(
                {"_id": ObjectId("6029b7f80febec6e0f942fcb")}, newshot)
            flash("Shotlist Successfully Updated")
            return redirect(url_for("user_home", username=session["user"]))

        return render_template("add_shotlist.html")

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    if session["user"] == "admin":
        if request.method == "POST":
            new_image = {
                "image_name": request.form.get("image_name"),
                "image_des": request.form.get("image_des"),
                "image_src": request.form.get("image_src")
            }
            mongo.db.images.insert_one(new_image)
            flash("Image Added")
            return redirect(url_for("user_home", username=session["user"]))

        return render_template("add_image.html")

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/remove_user", methods=["GET", "POST"])
def remove_user():
    if session["user"] == "admin":
        if request.method == "POST":
            mongo.db.users.remove({"firstname": request.form.get(
                "first_name"), "lastname": request.form.get("last_name")})
            flash("User Successfully Removed")
            return redirect(url_for("user_home", username=session["user"]))

        return render_template("remove_user.html")

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


@app.route("/delete_image/<image_id>")
def delete_image(image_id):
    if session["user"] == "admin":
        mongo.db.images.delete_one({"_id": ObjectId(image_id)})
        flash("Image Removed")
        return redirect(url_for("get_image"))

    else:
        flash("Entry Incorrect")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
