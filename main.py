#from Scripts.bottle import request
from flask import Flask, render_template, flash, request,session
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import mysql.connector
import tkinter.messagebox
#import os, shutil

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/admin")
def admin():

    return render_template('admin.html')
@app.route("/shome")
def shome():

    return render_template('shome.html')
@app.route("/view")
def view():


    return render_template('view.html')
@app.route("/view11", methods=['GET', 'POST'])
def view11():
    error = None
    if request.method == 'POST':
       date=request.form['date']
       conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
       cursor1 = conn1.cursor()
       cursor1.execute("SELECT * from visitors where date='"+date+"' ")
       data1 = cursor1.fetchall()

       return render_template('view.html', data=data1)


@app.route("/today")
def today():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
    cursor = conn.cursor()
    cursor.execute("SELECT * from visitors")
    data = cursor.fetchall()

    return render_template('today.html',data=data)
@app.route("/overall")
def overall():
    return render_template('overall.html')
@app.route("/user")
def user():
    return render_template('user.html')
@app.route("/views")
def viewu():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
    cursor = conn.cursor()
    cursor.execute("SELECT * from emp")
    data = cursor.fetchall()

    return render_template('views.html',data=data)
@app.route("/viewe")
def viewe():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
    cursor = conn.cursor()
    cursor.execute("SELECT * from emp")
    data = cursor.fetchall()

    return render_template('viewe.html',data=data)
@app.route("/viewg")
def viewg():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
    cursor = conn.cursor()
    cursor.execute("SELECT * from book where status='3'")
    data = cursor.fetchall()

    return render_template('viewg.html',data=data)


@app.route("/adminhome")
def adminhome():


    return render_template('adminhome.html')
@app.route("/about")
def about():


    return render_template('about.html')

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
           cursor1 = conn1.cursor()
           cursor1.execute("SELECT * from emp ")
           data1 = cursor1.fetchall()

           return render_template('adminhome.html',data1=data1)

       else:
        return render_template('index.html', error=error)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['fname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
        cursor = conn.cursor()
        cursor.execute("SELECT * from emp where uname='" + username + "' and psw='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
            cursor = conn.cursor()
            cursor.execute("SELECT * from emp where uname='" + username + "' and psw='" + password + "'")
            data = cursor.fetchone()
            name=data[1]
            session['eid']=data[0]

            return render_template('shome.html')



@app.route("/addsecurity", methods=['GET', 'POST'])
def addsecurity():
    if request.method == 'POST':

        name1 = request.form['name']

        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']

        phone = request.form['phone']

        shf = request.form['shift']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO emp VALUES ('','" + name1 + "','" + gender + "','" + age + "','"+ email+"','"+phone+"','" + address + "','" + shf + "','"+uname+"','"+password+"')")
        conn.commit()
        conn.close()


    return render_template('adminhome.html')

@app.route("/newvisitor", methods=['GET', 'POST'])
def newvisitor():
    if request.method == 'POST':
        import random

        otp=random.randint(1000, 9000)
        from datetime import date
        today = str(date.today())
        print(today)

        name1 = request.form['name']

        gender = request.form['gender']


        phone = request.form['phone']

        intime = request.form['intime']
        otime = request.form['otime']
        ublock = request.form['block']
        session['name']=name1



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO visitors VALUES ('','" + name1 + "','" + gender + "','" + today + "','"+ intime+"','"+otime+"','" + ublock + "','"+phone+"','"+str(otp)+"')")
        conn.commit()
        conn.close()


    return render_template('otp.html')

@app.route("/overalldata", methods=['GET', 'POST'])
def overalldata():
    error = None
    if request.method == 'POST':
       date=request.form['date']
       conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
       cursor1 = conn1.cursor()
       cursor1.execute("SELECT * from visitors where date='"+date+"' ")
       data1 = cursor1.fetchall()

       return render_template('overall.html', data=data1)

@app.route("/otp", methods=['GET', 'POST'])
def otp():
    error = None
    if request.method == 'POST':
       date=request.form['otp']
       name1=session['name']
       print(name1)
       print(date)
       conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='apartment')
       cursor1 = conn1.cursor()
       cursor1.execute("SELECT * from visitors where name='"+name1+"' and otp='"+date+"' ")
       data1 = cursor1.fetchone()
       if data1 is None:
           return 'OTP Password is wrong'
       else:
           return render_template('view.html')



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)