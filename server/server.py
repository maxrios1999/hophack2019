

from flask import Flask, request, abort, redirect, Response, url_for, render_template
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin):
    emails = {}
    numbers = {}

    def __init__(self, username, password, id, email, number, bussines_name, name, picture, active=True):
        self.id = id
        self.username = username
        self.password = password
        self.active = active
        self.email = email
        self.number = number
        self.bussines_name = bussines_name
        self.name = name
        self.picture = picture
        User.numbers[number] = self
        User.emails[email] = self

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.username, key='secret_key')


class UsersRepository:

    def __init__(self):
        self.users = dict()
        self.users_id_dict = dict()
        self.identifier = 0

    def save_user(self, user):
        self.users_id_dict.setdefault(user.id, user)
        self.users.setdefault(user.username, user)

    def get_user(self, username):
        return self.users.get(username, None)

    def get_user_by_id(self, userid):
        return self.users_id_dict.get(userid)

    def next_index(self):
        self.identifier += 1
        return self.identifier


users_repository = UsersRepository()


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registeredUser = users_repository.get_user(username)
        if registeredUser:
            print('Users ' + str(users_repository.users))
            print('Register user %s , password %s' %
                  (registeredUser.username, registeredUser.password))
            if registeredUser != None and registeredUser.password == password:
                print('Logged in..')
                login_user(registeredUser)
                return redirect(url_for('home'))
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        number = request.form['number']
        human_name = request.form['human_name']
        bussiness = request.form['bussiness']

        new_user = User(username, password, users_repository.next_index())
        users_repository.save_user(new_user)
        return Response("Registered Successfully")
    else:
        return Response('''
            <form action="" method="post">
            <p><input type=text name=username placeholder="Enter username">
            <p><input type=email name=email placeholder="Enter Email">
            <p><input type=password name=password placeholder="Enter password">
            <p><input type=text name=human_name placeholder="Enter your Name">
            <p><input type=text name=bussiness placeholder="Enter your bussiness' name">

            <p><input type=number name=number placeholder="Enter your phone number">
            <p><input type=submit value=Login>
            </form>
        ''')

# handle login failed
@app.errorhandler(401)
def failed_log_in(e):
    return Response('<p>Login failed</p>')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return users_repository.get_user_by_id(userid)


if __name__ == '__main__':
    app.run(debug=True)
