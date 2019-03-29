from flask import Flask, render_template
import json

app = Flask(__name__)
# app._static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("AboutUs.html")

if __name__ == "__main__":
    app.run(debug=True)