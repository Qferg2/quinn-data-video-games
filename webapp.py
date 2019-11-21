from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
        return render_template('home.html', options = get_game_options(game))
    
@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

@app.route("/p3")
def render_page3():
    return render_template('page3.html')
        
def get_game_options(games):
    options = ""
    listOfTitles = []
    for game in games:
        if game['Title'] not in listOfTitles:
            listOfTitles.append(game['Title'])
            
    for game in listOfTitles:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
        
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
