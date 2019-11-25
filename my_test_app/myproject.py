import pyrebase

from flask import Flask, render_template, session, redirect, url_for, escape, request
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

config = {
"apiKey": "AIzaSyDEmBuhMiLL9p9_3tiiN9I-Cm5Bhw995pQ",
    "authDomain": "test-6cea8.firebaseapp.com",
    "databaseURL": "https://test-6cea8.firebaseio.com",
    "projectId": "test-6cea8",
    "storageBucket": "test-6cea8.appspot.com",
    "messagingSenderId": "602926354722",
    "appId": "1:602926354722:web:1b09c98a1c3a9664bc557b",
    "measurementId": "G-B2T4NWHHF5"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("jioke.k@gmail.com", "codersworld")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing/<username>')
def landingPage():
    return render_template('landing.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    unsuccessful = 'Please check your credentials'
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        try:
             auth.sign_in_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('login.html', us=unsuccessful)
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])

def signup():
    error = None
    mesg = 'Please enter your credentials'
    unsuccessful = 'Username Exist, or password must be 6 characters'
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        try:
             user = auth.create_user_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('signup.html', us=unsuccessful)
    return render_template('signup.html', error=error)

@app.route('/logout')
def logout():
    #remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

'''
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
'''

if __name__ == '__main__':
    app.run()
