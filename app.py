from flask import Flask, render_template, request, url_for, redirect, session
import json
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
mysql = MySQL()
app = Flask(__name__)
# app._static_folder = 'static'
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'jsckp5HTKU'
app.config['MYSQL_PASSWORD'] = '9O5x78oQvj'
app.config['MYSQL_DB'] = 'jsckp5HTKU'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.secret_key = 'super_secret_key'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("AboutUs.html")

@app.route('/login', methods=['POST'])
def login():
    email= request.form['email']
    password= request.form['password'].encode('utf-8')
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user where email=%s",(email,))
    user = cur.fetchone()
    cur.close()
    print(type(user))
    if user is not None:
        if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
            session['name'] = user['firstname']
            session['email'] = user['email']
            return redirect(url_for('home'))
    else:
        return "Username or Password does not match"

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    firstname= request.form['firstname']
    lastname= request.form['lastname']
    email= request.form['email']
    password= request.form['password'].encode('utf-8')
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (firstname,lastname,email,password) VALUES(%s,%s,%s,%s)",(firstname,lastname,email,hash_password,))
    mysql.connection.commit()
    session['name']= firstname
    session['email'] = email
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
