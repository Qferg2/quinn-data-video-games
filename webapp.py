from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
        return render_template('home.html')
    
@app.route("/p1")
def render_page1():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
    return render_template('page1.html', options = get_game_options(games))
    
@app.route("/gameinfo")
def interesting_info():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
    game = request.args["game"]
    return render_template('page1.html', options = get_game_options(games), name = game, info = get_interesting_info(games, game), info1 = get_interesting_info1(games, game), info2 = get_interesting_info2(games, game), info3 = get_interesting_info3(games, game))

@app.route("/p2")
def render_page2():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
    return render_template('page2.html', yearOptions = get_year_options(games))
    
@app.route("/yearinfo")
def year_info():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
    year = request.args["year"]
    return render_template('page2.html', options = get_game_options(games), yearInfo = get_year_info(games, year), yearInfo1 = get_year_info1(games, year))

@app.route("/p3")
def render_page3():
    return render_template('page3.html')
        
def get_interesting_info(games, game):
    for data in games:
        if data['Title'] == game:
            return data['Release']['Console']
            
def get_interesting_info1(games, game):
    for data in games:
        if data['Title'] == game:
            return data['Release']['Year']
            
def get_interesting_info2(games, game):
    for data in games:
        if data['Title'] == game:
            return data['Metrics']['Sales']
            
def get_interesting_info3(games, game):
    for data in games:
        if data['Title'] == game:
            return data['Metrics']['Review Score']
            
def get_year_info(games, year):
    max = games[0]['Metrics']['Sales']
    game = games[0]['Title']
    for data in games:
        if data['Release']['Year'] == year:
            if data['Metrics']['Sales'] > max:
                max = data['Metrics']['Sales']
                game = data['Title']
    return game
    
def get_year_info1(games, year):
    max = games[0]['Metrics']['Sales']
    for data in games:
        if data['Release']['Year'] == year:
            if data['Metrics']['Sales'] > max:
                max = data['Metrics']['Sales']
    return max
        
def get_game_options(games):
    options = ""
    listOfTitles = []
    for game in games:
        if game['Title'] not in listOfTitles:
            listOfTitles.append(game['Title'])
            
    for game in listOfTitles:
        options = options + Markup("<option value=\"" + game + "\">" + game + "</option>")
    return options
    
def get_year_options(games):
    yearOptions = ""
    listOfYears = []
    for year in games:
        if year['Release']['Year'] not in listOfYears:
            listOfYears.append(year['Release']['Year'])
            
    for year in listOfYears:
        yearOptions = yearOptions + Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
    return yearOptions
        
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
