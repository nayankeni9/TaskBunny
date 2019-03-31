from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)
# app._static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("AboutUs.html")

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print('The url is here'+request.form['email']+'   '+request.form['password'])
        return redirect(url_for('home'))
    else:
        print('error')

if __name__ == "__main__":
    app.run(debug=True)
