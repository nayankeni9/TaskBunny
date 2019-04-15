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
    if user is not None:
        if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
            session['name'] = user['firstname']
            session['email'] = user['email']
            session['type'] = 'USER'
            return redirect(url_for('home'))
    else:
        return "Username or Password does not match"

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
    global user
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
    session['type'] = 'USER'
    cur.execute("SELECT * FROM user where email=%s",(session['email'],))
    user = cur.fetchone()
    cur.close()
    return redirect(url_for('home'))


@app.route('/tasker_login', methods=['POST'])
def tasker_login():
    email= request.form['email']
    password= request.form['password'].encode('utf-8')
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasker where email=%s",(email,))
    user = cur.fetchone()
    cur.close()
    if user is not None:
        if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
            session['name'] = user['firstname']
            session['email'] = user['email']
            session['type'] = 'TASKER'
            return redirect(url_for('home'))
    else:
        return "Username or Password does not match"

@app.route("/tasker_logout")
def tasker_logout():
    session.clear()
    return render_template("index.html")

@app.route('/tasker_register', methods=["POST"])
def tasker_register():
    firstname= request.form['firstname']
    lastname= request.form['lastname']
    email= request.form['email']
    contact=request.form['contact']
    password= request.form['password'].encode('utf-8')
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasker (firstname,lastname,email,password,contact_number) VALUES(%s,%s,%s,%s,%s)",(firstname,lastname,email,hash_password,contact))
    mysql.connection.commit()
    cur.close()
    session['name']= firstname
    session['email'] = email
    session['type'] = 'TASKER'
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user where email=%s",(session['email'],))
    user = cur.fetchone()
    cur.close()
    session['mode']='READONLY'
    session['name']= user['firstname']
    return render_template("profile.html", user=user)

@app.route('/save_user' , methods=["POST"])
def save_user():
    global user
    firstname= request.form['firstname']
    lastname= request.form['lastname']
    email= request.form['email']
    contact_number=request.form['contact_number']
    street_address=request.form['street_address']
    city=request.form['city']
    state=request.form['state']
    zip=request.form['zip']
    cur = mysql.connection.cursor()
    print(firstname,lastname,contact_number, street_address, city, state, zip ,email)
    cur.execute("""UPDATE user 
                set firstname=%s,
                lastname =%s,
                contact_number=%s,
                street_address=%s,
                city=%s,
                state=%s,
                zip=%s
                where email = %s 
                """,
                (firstname,lastname,contact_number, street_address, city, state, zip ,session['email'],))
    mysql.connection.commit()

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user where email=%s",(session['email'],))
    user = cur.fetchone()
    cur.close()
    return redirect(url_for('profile'))

@app.route('/edit_user')
def edit_user():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user where email=%s",(session['email'],))
    user = cur.fetchone()
    cur.close()
    session['mode']='EDIT'
    return render_template("profile.html", user=user)

@app.route('/tasker_profile')
def tasker_profile():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasker where email=%s",(session['email'],))
    tasker = cur.fetchone()
    cur.execute("SELECT Service_Id,Service_Name FROM Service")
    services = cur.fetchall()
    cur.close()
    session['mode']='READONLY'
    session['name']= tasker['firstname']
    return render_template("tasker_profile.html", tasker=tasker, services=services)

@app.route('/save_tasker' , methods=["POST"])
def save_tasker():
    firstname= request.form['firstname']
    lastname= request.form['lastname']
    email= request.form['email']
    contact_number=request.form['contact_number']
    street_address=request.form['street_address']
    city=request.form['city']
    state=request.form['state']
    zip=request.form['zip']
    primary_skill = int(request.form['service_category'])
    tasker_age= request.form['age']
    cur = mysql.connection.cursor()
    print(firstname,lastname,contact_number, street_address, city, state, zip ,email, primary_skill)
    cur.execute("""UPDATE tasker 
                set firstname=%s,
                lastname =%s,
                contact_number=%s,
                street_address=%s,
                city=%s,
                state=%s,
                zip=%s,
                primary_skill=%s,
                tasker_age = %s
                where email = %s 
                """,
                (firstname,lastname,contact_number, street_address, city, state, zip ,primary_skill, tasker_age, session['email'],))
    mysql.connection.commit()

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasker where email=%s",(session['email'],))
    tasker = cur.fetchone()
    cur.close()
    return redirect(url_for('tasker_profile'))

@app.route('/edit_tasker')
def edit_tasker():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM tasker where email=%s",(session['email'],))
    tasker = cur.fetchone()
    cur.execute("SELECT Service_Id,Service_Name FROM Service")
    services = cur.fetchall()
    cur.close()
    session['mode']='EDIT'
    return render_template("tasker_profile.html", tasker=tasker, services=services)

@app.route('/home_services')
def home_services():
    return render_template("home_services.html")

@app.route("/book")
def book():
    return render_template("booking.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
