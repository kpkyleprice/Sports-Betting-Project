from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from helpers import token_required
from models import db, User, Bet, bet_schema, bets_schema
from flask_login import current_user, login_required

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/nbanews')
def nbanews():
    return render_template('nbanews.html')
    
@site.route('/nflnews')
def nflnews():
    return render_template('nflnews.html')

@site.route('/mlbnews')
def mlbnews():
    return render_template('mlbnews.html')

@site.route('/ncaambnews')
def ncaambnews():
    return render_template('ncaambnews.html')
    
@site.route('/nhlnews')
def nhlnews():
    return render_template('nhlnews.html')

@site.route('/wnbanews')
def wnbanews():
    return render_template('wnbanews.html')

@site.route('/boxingnews')
def boxingnews():
    return render_template('boxingnews.html')

@site.route('/nba')
def nba():
    return render_template('nba.html')
    
@site.route('/nfl')
def nfl():
    return render_template('nfl.html')

@site.route('/mlb')
def mlb():
    return render_template('mlb.html')

@site.route('/ncaamb')
def ncaamb():
    return render_template('ncaamb.html')
    
@site.route('/nhl')
def nhl():
    return render_template('nhl.html')

@site.route('/wnba')
def wnba():
    return render_template('wnba.html')

@site.route('/boxing')
def boxing():
    return render_template('boxing.html')

@site.route('/calculator')
def calculator():
    return render_template('parlay.html')
   




@site.route("/bets")
def Bets():
    bets = Bet.query.all()
    return render_template("bets.html",bets=bets)

@site.route('/add_bet', methods=['POST'])
def add_bet():
    print('add_bet')
    amount = request.form['Amount']
    team = request.form['Team']
    odds = request.form['Odds']
    user_id = current_user.id

    print(amount,team,odds,user_id)

    bet = Bet(Amount=amount, Team=team, Odds=odds, user_id=user_id)
    db.session.add(bet)
    db.session.commit()
    
    return redirect(url_for('site.Bets'))

@site.route('/delete_bet/<id>', methods=['POST'])
def delete_bet(id):
    bet = Bet.query.get(id)
    if bet:
        if bet.user_id == current_user.id:
            db.session.delete(bet)
            db.session.commit()
            return jsonify({'message': 'Bet was successfully removed.'})
        else: 
            return jsonify({'message': 'You do not have permission to delete this bet.'})
    else:
        return jsonify({'message': 'Error bet not found.'})
    return redirect(url_for('site.bets')) 

@site.route("/show_bet/<id>", methods =['POST'])
def show_bet(id):
    bet = Bet.query.get(id)
    if request.method == 'POST':
        return render_template("update_bets.html",bet=bet)

@site.route('/update_bet/<id>', methods=['POST'])
def update_bet(id):
    bet = Bet.query.get(id)

    if not bet:
        return jsonify({'message': 'Error: Bet not found.'})

    if bet.user_id != current_user.id:
        return jsonify({'message': 'Error: You do not have permission to update this bet.'})

    if request.method == 'POST':
        amount = request.form['Amount']
        team = request.form['Team']
        odds = request.form['Odds']
# request.form causing issues werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
# KeyError: 'Amount'
        bet.Amount = amount
        bet.Team = team
        bet.Odds = odds

        db.session.commit()

        return redirect(url_for('site.Bets'))

    return render_template('update_bets.html', bet=bet)