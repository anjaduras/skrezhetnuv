from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)
