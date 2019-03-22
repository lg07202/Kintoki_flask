from flask import Flask,request,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////mnt/c/Users/Haider/Documents/flask_app/kintoki.db'
db=SQLAlchemy(app)

class Post(db.Model):
	id=db.Column(db.Integer,primary_key =True)
	title= db.column(db.String(50))
	subtitle=db.column(db.String(50))
	author=db.column(db.String(20))
	date_posted=db.Column(db.DateTime)
	content=db.column(db.Text)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/post')
def post():
	return render_template('post.html')
@app.route('/contact',  methods=['GET','POST'])
def contact():
	return render_template('contact.html')
@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/addpost', methods=['GET','POST'])
def addpost():
	title=request.form['title']
	subtitle=request.form['subtitle']
	author =request.form['author']
	content=request.form['content']
	
	post= Blogpost(title=title, subtitle=subtitle,author=author,content=content)
	db.session.add(post)
	db.session.commit()
	return redirect(url_for('index'))
if __name__=="__main__":
     app.run(debug=True)
     