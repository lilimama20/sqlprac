from flask import Flask, render_template,request, redirect, url_for
from flask_mysqldb import MySQL

app= Flask(__name__)

#configure mysql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ifeoluwa123.'
app.config['MYSQL_DB']='FLASK_APP'
app.config['MYSQL_CURSORCLASS']='DictCursor'


#Initialize MySQL
mysql=MySQL(app)
@app.route('/')
def index():
    try:
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM EXAMPLE_table")
        data = cur.fetchall()
        cur.close()
        return render_template("/index.html", data=data)
    except Exception as e:
        print(e)

@app.route('/add_user', methods=['POST','GET'])
def add_user():
    try:
        if request.method == 'POST':
            name= request.form['name']
            email = request.form['email']

            cur= mysql.connection.cursor()
            cur.execute('insert into example_table (name, email) VALUES(%s, %s)', (name,email))
            mysql.connection.commit()
            cur.close()

            return redirect(url_for('index'))
    except Exception as e:
        print(e)
    return render_template("add_user.html")

if __name__ == '__main__':
    app.run(debug=True)
