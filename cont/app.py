from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def aboutme():
    return render_template("aboutme.html")

@app.route("/favs")
def lectures():
    return render_template("lectures.html")

@app.route("/lectures")
def favs():
    return render_template("favs.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))