from flask import *

app = Flask(__name__)

# 起動時、login画面遷移
@app.route("/")
def jump():
    return redirect("/login")

# login画面表示
@app.route('/login')
def index():
    return render_template('login.html')
