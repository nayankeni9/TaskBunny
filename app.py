from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import json
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import imagesrc
import random

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
    about_me = request.form['about_me']
    cur = mysql.connection.cursor()
    cur.execute("""UPDATE tasker 
                set firstname=%s,
                lastname =%s,
                contact_number=%s,
                street_address=%s,
                city=%s,
                state=%s,
                zip=%s,
                primary_skill=%s,
                tasker_age = %s,
                about_me=%s
                where email = %s 
                """,
                (firstname,lastname,contact_number, street_address, city, state, zip ,primary_skill, tasker_age, about_me, session['email'],))
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

@app.route("/tasker_list")
def tasker_list():
    category = request.args.get("category")
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""SELECT * FROM tasker where primary_skill=%s and 
                    tasker.id not in(select Tasker_Id from `Task_Assignment` where Task_Status = 'PENDING')""",(category))
    tasker_list = cur.fetchall()
    cur.close()
    tasker_json = []
    for tasker in tasker_list:
        tasker_obj={"id": tasker['id'],
                      "Service_Id": tasker['Service_Id'], 
                      "firstname": tasker['firstname'], 
                      "lastname": tasker['lastname'], 
                      "contact_number": tasker['contact_number'], 
                      "email": tasker['email'],
                      "street_address": tasker['street_address'],
                      "city": tasker['city'],
                      "state": tasker['state'],
                      "zip": tasker['zip'], 
                      "primary_skill": tasker['primary_skill'], 
                      "tasker_age": tasker['tasker_age'],
                      "about_me": tasker['about_me'], 
                      "vehicle_owned": tasker['vehicle_owned'], 
                      "reward": tasker['reward'], 
                      "is_active": tasker['is_active'],
                      "image": imagesrc.tasker_images[tasker['id']],
                      "service_rate": tasker['service_rate']
                    }
        tasker_json.append(tasker_obj)
    print(tasker_json)
    return jsonify({"tasker_list": tasker_json})

@app.route("/order" , methods=["POST"])
def order():
    service_name = request.form['preview_service']
    service_type_name = request.form['preview_service_type']
    service_date = request.form['preview_date']
    service_time = request.form['preview_time']
    service_location = request.form['preview_location']
    service_address = request.form['preview_address']
    service_tasker_name = request.form['preview_service_type']
    service_tasker_email = request.form['preview_tasker_email']
    service_time = request.form['preview_time']
    service_description = request.form['preview_description']
    primary_key = random.randint(1, 9999999)

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""INSERT INTO `Order`(Order_Id, User_Id, Service_Id, Order_Date, Service_Type, Service_Description, Service_Date, Service_Time)
                   values (%s,
                           (select id from user where email = %s),
                           (select Service_Id from Service where trim(Service_name) = trim(%s)),
                           CURDATE(),
                           %s,
                           %s,
                           %s,
                           %s
                           )""",(primary_key, session['email'], service_name, service_type_name, service_description, service_date, service_time))


    cur.execute("""INSERT INTO `Task_Assignment`(Tasker_Id, Order_Id, Task_Status)
                VALUES(
                    (select id from tasker where email = %s),
                    %s,
                    'PENDING'
                )""", (service_tasker_email, primary_key))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
