import json
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "@@thisismysecret@@"

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		formData = request.form.to_dict()
		tempUser, tempPwd = formData["username"], formData["password"]
		correctUser, correctPwd = False, False
		with open("accounts.json") as f:
			accountData = json.load(f)
			for user in accountData:
				for value in accountData[user].values():
					if value == tempUser:
						correctUser = True
					elif value == tempPwd:
						correctPwd = True
					else:
						continue
			if (correctUser) and (correctPwd):
				flash(f"Logged into account {form.username.data}!", "success")
				return redirect(url_for("home"))
			else:
				flash("Error while logging in!", "danger")
	else:
		if request.method == "POST":
			flash("Error while logging in!", "danger")
	return render_template("login.html", title="Login", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	temp = {}
	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}!", "success")
		formData = request.form.to_dict()
		temp = {
			"username": formData["username"],
			"password": formData["password"]
		}
		with open("accounts.json") as f:
			accountData = json.load(f)
			accountData[formData["username"]] = temp
		with open("accounts.json", "w") as f:
			json.dump(accountData, f)
		return redirect(url_for("home"))
	else:
		if request.method == "POST":
			flash("Error while creating an account!", "danger")
	return render_template("register.html", title="Register", form=form)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

if __name__ == "__main__":
	app.run(debug=True)
