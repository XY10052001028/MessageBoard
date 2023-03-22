from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/")
def index():
    return render_template("index.html.jinja2", messages=messages)

@app.route("/post/add/", methods=["POST"])
def add_post():
    content = request.form["content"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append((content, timestamp))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True) 