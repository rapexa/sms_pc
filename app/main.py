import requests
import config
import MySQLdb
from flask import Flask, flash, jsonify, redirect, request, render_template, url_for, Response, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# config
app.config.update(
    SECRET_KEY = config.secret_key
)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        
    def __repr__(self):
        return "%d" % (self.id)


# create some users with ids 1 to 20       
user = User(0)

@app.errorhandler(404)
@login_required
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash
    return redirect('login')   
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid) 

@app.route("/ok")
def sys_check():
    '''this function tell that falsk server is ok and running!!'''
    ret = {'status':'ok','message':'[+] flask server is running'}
    return jsonify(ret) , 200

@app.route("/message_Send")
@login_required
def message_Send():
    '''this is test subject for message_Send'''
    return render_template("sendedsms.html")

@app.route("/get_sms_from",methods=["GET", "POST"])
def get_sms_from():
    if request.method == 'POST':
        data = request.form
        sender = data["from"]
        message = data["message"]
        writing_sms_to_database("دریافت",sender,message)
        redirect(url_for('get_sms_from'))
    return redirect(url_for('get_sms_from'))    

@app.route("/get_sms",methods=["GET", "POST"])
@login_required
def get_sms():
    '''this is getting sms function'''
    all_sms = reading_smss_from_database()
    smss = []
    for work in all_sms:
        status, sender, message = work
        smss.append({"status":status,"sender":sender,"message":message})
    return render_template("getsms.html", data = {"smss" : smss})   

@app.route("/",methods=["GET", "POST"])
@login_required
def send_sms(): 
    '''this function send sms'''
    if request.method == 'POST':
        phone = request.form["phone"]
        message = request.form["message"]
        sendsms(phone,message)
        writing_sms_to_database("ارسال",phone,message)
        return redirect("message_Send")      

    else:
        return render_template('send.html')    

@app.route("/login",methods=["GET", "POST"])
@limiter.limit("10 per minute")
def login():
    '''this function return login page'''
    message = None
    if current_user.is_authenticated:
        return redirect(url_for("get_sms"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check(username,password):
            login_user(user)
            flash('ورود به سرور موفق','info')
            return redirect(url_for('get_sms'))
        else:
            message = 'نام کاربری یا رمز عبور اشتباه می باشد'

    return render_template('login.html', message=message)            

def sendsms(phone,mess):
    url = config.url
    data = {'receptor':phone, 'message':mess}
    respon = requests.post(url,data=data)
    return respon

def check(username,password):
    res = False
    usernamein = config.username
    passwordin = config.password
    if username == usernamein and password == passwordin:
        res = True
    return res    

def writing_sms_to_database(status,sender,message):
    db = connect_to_database()    
    cur = db.cursor()
    qury = f'INSERT INTO messages VALUES ("{status}","{sender}","{message}");'
    cur.execute(qury)
    db.commit()
    db.close()

def reading_smss_from_database():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute("SELECT * FROM messages;")
    db.close()
    return cur.fetchall()

def connect_to_database():
    db = MySQLdb.connect(host=config.MYSQL_HOST,
                       user=config.MYSQL_USER,
                       passwd=config.MYSQL_PASS,
                       db=config.MYSQL_DB,
                       charset=config.charset)
    return db                       

if __name__ == "__main__":
    app.run("0.0.0.0",5000,debug=True)