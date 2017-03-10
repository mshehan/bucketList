from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['DEBUG'] = True 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thankyou2'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route("/signUp", methods=['POST'])
def signUp():
    #read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash( _password)
    if _name and _email and _password:
        print(_hashed_password)
        cursor.callproc('sp_createUser',( _name, _email, _hashed_password))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({
                'message':'User created successfully ! ',
                'picurl' : 'abc.com/123',
                'name': str(_name)
            })
        else:
            return json.dumps({'error':str(data[0])})
   
    return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route("/showSignIn")
def showSignIn():
    return render_template('signin.html')

@app.route("/signin", methods=['POST'])
def signin():
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash(_password)
    if _email and _password:
        print(_hashed_password)
        statement = "SELECT * FROM BucketList.tbl_user WHERE user_username = %(_email)s"
        cursor.execute(statement, {'_email': _email})
        data = cursor.fetchone()
        if data is not None:
            return json.dumps({"message": "successful login", "redirect":"http://tinyurl.com/", "data": data})
        
        else:
            return json.dumps({'error': 'request failed'})
        

if __name__ == "__main__":
    app.run()

