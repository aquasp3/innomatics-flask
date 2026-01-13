from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/match", methods=["POST"])
def match():
    text = request.form["text"]
    pattern = request.form["pattern"]

    try:
        matches = re.findall(pattern, text)
    except re.error:
        matches = []

    return render_template("result.html", matches=matches)

if __name__ == "__main__":
    app.run(debug=True)
