from flask import Flask, render_template, redirect, url_for
from data import ALL_RESULTS, fixtures, ALL_CLUBS, ALL_PLAYERS, PREMIER_LEAGUE
from numpy import zeros
import user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html', messages=None)

@app.route('/squad')
def squad():
    rows =zeros((9, 9))
    return render_template('squad.html', rows=rows, club=user.CLUB)

@app.route('/view_player/<id>')
def view_player(id):
    player = [player for player in ALL_PLAYERS if player._id == int(id)][0]
    return render_template('view_player.html', player=player)

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
    PREMIER_LEAGUE.order_table()
    return render_template('competition.html', 
        clubs=ALL_CLUBS, all_results=ALL_RESULTS, league_name="Premier League")

@app.route("/competition/stats")
def competition_stats():
    PREMIER_LEAGUE.order_table()

    total_w = 0
    total_d = 0
    total_l = 0
    total_ga = 0
    total_gf = 0
    total_gd = 0
    total_pts = 0
    for club in ALL_CLUBS:
        total_w += club.W
        total_d += club.D
        total_l += club.L
        total_ga += club.GA
        total_gf += club.GF
        total_gd += club.GD
        total_pts += club.PTS

    win_avg = round(total_w / len(ALL_CLUBS), 2)
    draw_avg = round(total_d / len(ALL_CLUBS), 2)
    loss_avg = round(total_l / len(ALL_CLUBS), 2)
    ga_avg = round(total_ga / len(ALL_CLUBS), 2)
    gf_avg = round(total_gf / len(ALL_CLUBS), 2)
    gd_avg = round(total_gd / len(ALL_CLUBS), 2)
    pts_avg = round(total_pts / len(ALL_CLUBS), 2)

    avarages = {
        "W": win_avg,
        "D": draw_avg,
        "L": loss_avg,
        "GA": ga_avg,
        "GF": gf_avg,
        "GD": gd_avg,
        "PTS": pts_avg
    }

    for club in ALL_CLUBS:
        club.win_rate = round(club.W / win_avg, 2)
        club.draw_rate = round(club.D / draw_avg, 2)
        club.loss_rate = round(club.L / loss_avg, 2)
        club.ga_rate = round(club.GA / ga_avg, 2)
        club.gf_rate = round(club.GF / gf_avg, 2)
        club.pts_rate = round(club.PTS / pts_avg, 2)
    return render_template('competition_stats.html', avarages=avarages,
        clubs=ALL_CLUBS, all_results=ALL_RESULTS, league_name="Premier League")

@app.route('/view_club/<id>')
def view_club(id):
    for pos, club in enumerate(ALL_CLUBS, start=1):
        if club._id == int(id):
            squad = []
            for player in club.squad:
                if player not in squad: squad.append(player)
                
            club.squad = squad
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