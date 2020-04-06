from flask import Flask,render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)
conn=pymysql.connect('localhost','root','qazxsw','users')

@app.route("/")
def showData():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from users")
        rows=cur.fetchall()
    return render_template('index.html',datas=rows)

@app.route("/user")
def showForm():
    return render_template('adduser.html')


@app.route("/insert",methods=['POST'])
def insert():
    if request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        with conn.cursor() as cursor:
            sql = "insert into users (username,email,mobile) values (%s,%s,%s)"
            cursor.execute(sql,(username,email,mobile))
            conn.commit()
        return redirect(url_for('showData'))

@app.route("/update",methods=['POST'])
def update():
    if request.method=="POST":
        id_update = request.form['id']
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        with conn.cursor() as cursor:
            sql = "update users set username=%s,email=%s,mobile=%s where id=%s"
            cursor.execute(sql,(username,email,mobile,id_update))
            conn.commit()
        return redirect(url_for('showData'))

@app.route("/add",methods=['POST'])
def add():
    if request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        with conn.cursor() as cursor:
            sql = "insert into users (username,email,mobile) values (%s,%s,%s)"
            cursor.execute(sql,(username,email,mobile))
            conn.commit()
        return redirect(url_for('showData'))


@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn:
        cur=conn.cursor()
        cur.execute("delete from users where id=%s",(id_data))
        conn.commit()
    return redirect(url_for('showData'))


if __name__== "__main__":
    app.run(debug=True)