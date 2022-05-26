from asyncio import FastChildWatcher
from distutils.log import debug
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)


    def __repr__(self):
        return '<Users %r>' % self.id




@app.route('/addedusers')
def added_users():
    users = Users.query.all()
    return render_template("addedusers.html", users=users)



@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-users', methods = ['GET', 'POST'])
def create_users():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        users = Users(name=name, password=password)

        try:
            db.session.add(users)
            db.session.commit()
            return redirect('/addedusers')
        except:
            return "Error!"
    else:
         return render_template("create-users.html")




if __name__ == "__main__":
    app.run(debug=True)

