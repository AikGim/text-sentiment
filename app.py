from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
        return render_template("index.html")

@app.route("/result", methods = ["GET", "POST"])
def result():
    text = request.form.get("text")
    result = TextBlob(text).sentiment
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run()