from flask import Blueprint, render_template

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

    # add news and odds pages here maybe will see if login allows links to be navigatable 