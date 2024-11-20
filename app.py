from flask import Flask, render_template, session, request
from flaskext.mysql import MySQL
import pymysql

mysql =MySQL()
app = Flask(__name__, template_folder='templates')

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'crud'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    text=""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO accounts VALUES(NULL, %s, %s, %s)", (username, email, password,))
        conn.commit()
        text="added"

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
