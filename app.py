from flask import *

app = Flask(__name__)

# 起動時、login画面遷移
@app.route("/")
def jump():
    return redirect("/login")

# login画面表示
@app.route('/login', methods=['GET','POST'])
def index():
    username = None
    password = None
    error = None
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    if username and password == "password":  
        return redirect(url_for('select'))
    else:
        error = "Invalid username or password."  

    return render_template('login.html',error=error)

# ChatBot選択画面への遷移
@app.route('/select')
def select():
    return render_template('select.html')