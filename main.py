from flask import Flask, render_template, request
from everyform import *
from datafetch import *

app = Flask (__name__)
app.secret_key = "nota"
#only usable in my local machine
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:balepo@localhost/nus"
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/iniciar")
def login():
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def signup():
    forma = registerform()

    if forma.validate_on_submit():
        username = forma.username.data
        password = forma.password.data
        user = users(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "ok"
    else:
        for error in forma.errors:
            print(error)
    return render_template("signup.html", form = forma)

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.errorhandler(404)
def notfound(e):
    return render_template("404.html"), 404#render a custom template


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")
