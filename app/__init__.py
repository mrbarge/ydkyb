from flask import Flask, session, redirect, url_for, request, render_template
from app.ydkbengine import ydkbengine
from random import shuffle
import os

app = Flask(__name__)
app.config.from_object('app.config')
# test the API key for steam has been set
if not app.config['STEAM_API_KEY']:
	raise Exception("Must define STEAM_API_KEY in application config.")

@app.route('/', methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		session['username'] = request.form['username']
		session['statusscale'] = 100
		app.ydkbengine = ydkbengine(app.config['STEAM_API_KEY'],session['username'])
		return redirect(url_for('play'))
	else:
		return render_template('index.html')

@app.route('/gabe')
def gabe():
        return render_template('gabe.html')

@app.route('/play',methods=['GET','POST'])
def play():
	if request.method == 'GET':
		ownedgame = app.ydkbengine.pickOwnedGame(0)
		othergames = app.ydkbengine.pickOtherGames(2)
		# put all games in a list and shuffle them
		choicegames = [ownedgame] + othergames
		shuffle(choicegames)
		session['correctanswer'] = ownedgame[0]
		return render_template('play.html',choices=choicegames,scale=session['statusscale'])
	else:
		answer = request.form['answer']
		if str(answer) == str(session['correctanswer']):
			resultmsg = "congratulations, gabe is pleased"
			if session['statusscale'] > 100:
				session['statusscale'] -= 100
		else:
			resultmsg = "failure, gabe is displeased"
			if session['statusscale'] < 500:
				session['statusscale'] += 100
		ownedgame = app.ydkbengine.pickOwnedGame(0)
		othergames = app.ydkbengine.pickOtherGames(2)
		choicegames = [ownedgame] + othergames
		shuffle(choicegames)
		session['correctanswer'] = ownedgame[0]
		return render_template('play.html',resultmsg=resultmsg,choices=choicegames,scale=session['statusscale'])

if __name__ == '__main__':
	app.run(debug=True)
