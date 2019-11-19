from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    with open('video_games.json') as videogame_data:
        games = json.load(videogame_data)
        return render_template('home.html')
        
        
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
