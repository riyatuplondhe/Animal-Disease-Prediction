from flask import Flask, render_template, request, flash, redirect, url_for
import os
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "manthan"

@app.route("/")
def base():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

contact_files = "contact_messages.csv"
FIELDS = ["timestamp", "name", "email", "message"]
def ensure_file():
    if not os.path.exists(contact_files):
        with open(contact_files, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)

def save_message(name, email, message):
    ensure_file()

    with open(contact_files, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, email,   message
        ])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if name == "" or email == "" or message == "":
            flash("Please fill all fields")
            return redirect(url_for("contact"))

        try:
            save_message(name, email, message)
            flash("Message saved successfully")
        except Exception as e:
            flash("Error saving message")

        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

app.run(debug=True)
