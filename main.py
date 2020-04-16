from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "@@thisismysecret@@"
logins = {
	"admin": "password"
}

@app.route("/")
def login():
    return render_template("login.html", logins=logins)

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template("register.html", title="Register", form=form)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
	app.run(debug=True)
