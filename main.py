from flask import Flask, render_template, request, url_for, redirect
from everyform import *
from datafetch import *

app = Flask (__name__)
app.secret_key = "temporal"
#only usable in my local machine
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/sys"
db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/iniciar", methods=["GET", "POST"])
def login():#fincion debe enviar una cookie y enviar a HOME
    login_form = loginform()
    if login_form.validate_on_submit():
        print("meh")

    return render_template("login.html", form = login_form)

@app.route("/registro", methods=["GET", "POST"])
def signup():
    forma = registerform()

    if forma.validate_on_submit():
        #crea variables locales
        username = forma.username.data
        password = forma.password.data
        #pasa argumentos locales a la clase creada en datafetch
        user = userName(UID=username, Passkey=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
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
