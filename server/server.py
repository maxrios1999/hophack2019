from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask_login import LoginManager, login_required, login_user, logout_user
from components.users import User
app = Flask(__name__)

global number_of_users
number_of_users = 1
users = {}
# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/user/<username>", methods=["POST", "GET"])
@login_required
def my_profile(username):
    user = users.get


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        new_user = User(number_of_users, username, password)
        users[username] = new_user
        number_of_users += 1
        return "congrats"
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


if __name__ == "__main__":
    app.run()
