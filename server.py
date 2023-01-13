import flask
app = flask.Flask(__name__)

class Config():
    SECRET_KEY = "DJFAJLAJAFKLJQ"

app.config.from_object(Config())

@app.route('/login',methods = ["GET","POST"])
def login():
    
    if flask.request.method =="GET":
        return flask.render_template('login.html')
    else:
        name = flask.request.form.get("name")
        flask.session['username'] = name
        return flask.redirect(url_for('index'))

@app.route('/register',methods = ["GET","POST"])
def register():
    
    if flask.request.method =="GET":
        return flask.render_template('register.html')
    else:
        name = flask.request.form.get("name")
        password = flask.request.form.get("password")
        flask.session['username'] = name
        flask.session['password'] = password

        return flask.redirect(url_for('index'))

@app.route('/')
def index():
    return flask.render_template('index.html')
    


app.run()