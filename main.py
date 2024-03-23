from flask import Flask, render_template
from data import ALL_CLUBS, fixtures, LegendsLeague

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
    return render_template('competition.html', clubs=ALL_CLUBS)

@app.route('/scouting')
def scouting():
    return render_template('scouting.html')

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