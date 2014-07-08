from flask import Flask, session, redirect, url_for, escape, request, render_template
from app import app

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	if 'username' in session:
		return render_template('play.html')
#		return 'sup %s' % escape(session['username'])
	else:
		return render_template('index.html')

app.secret_key = '\xf4\xe7\xb5+M\xee\x0c\x10\x8e\xec\xc7\xc9\x10@P\xadG\x8a\x93\xd9\x06\x95\x1a)'
