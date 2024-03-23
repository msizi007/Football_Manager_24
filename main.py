from flask import Flask, render_template, redirect, url_for
from data import ALL_CLUBS, ALL_RESULTS, fixtures, LegendsLeague

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html', messages=None)

@app.route('/squad')
def squad():
    return render_template('squad.html')

@app.route('/tactics')
def tactics():
    return render_template('tactics.html')

@app.route('/squad_planner')
def squad_planner():
    return render_template('squad_planner.html')

@app.route('/data_hub')
def data_hub():
    return render_template('data_hub.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/medical_centre')
def medical_centre():
    return render_template('medical_centre.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/competition')
def competition():
    LegendsLeague.order_table()
    return render_template('competition.html', clubs=ALL_CLUBS, all_results=ALL_RESULTS)

@app.route('/view_club/<id>')
def view_club(id):
    for pos, club in enumerate(ALL_CLUBS, start=1):
        if club._id == int(id):
            return render_template('view_club.html', club=club, league_position=pos) 
        
    return redirect(url_for('competition'))

@app.route('/scouting')
def scouting():
    return render_template('scouting.html')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

@app.route('/club_info')
def club_info():
    return render_template('club_info.html')

@app.route('/club_vision')
def club_vision():
    return render_template('club_vision.html')

@app.route('/finances')
def finances():
    return render_template('finances.html')

if __name__ == "__main__":
    app.run(debug=True)