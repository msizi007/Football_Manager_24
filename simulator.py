import random
from statistics import mean

def round_off(x: float):
    x = str(x)
    number, decimals = x.split('.')
    number = int(number)
    if int(decimals[0]) >= 5:
        number +=1

    return int(number)

def simulate_fixture(team1, team2):
    team1.P += 1; team2.P += 1
    team1_avg = team1.avg
    team2_avg = team2.avg
    match_mean = mean([team1_avg, team2_avg])
    team1_rate = team1_avg/match_mean
    team2_rate = team2_avg/match_mean
    if team1_rate > team2_rate:
        team1_score = team1_rate+random.randint(0, round_off(team1_rate))+(random.random()*team1_rate)
        team2_score = team2_rate
    elif team1_rate < team2_rate:
        team2_score = team2_rate+random.randint(0, round_off(team2_rate))+(random.random()*team2_rate)
        team1_score = team1_rate
    else:
        team1_score = team1_rate+random.randint(0, round_off(team1_rate))+(random.random()*team1_rate)
        team2_score = team2_rate+random.randint(0, round_off(team2_rate))+(random.random()*team2_rate)
    
    team1_score = round_off(team1_score)
    team2_score = round_off(team2_score)
    
    if team1_score > team2_score:
        team1.W += 1; team2.L += 1
    elif team1_score < team2_score:
        team2.W += 1; team1.L += 1
    else:
        team1.D += 1; team2.D += 1

    team1.GA += team1_score; team1.GF += team2_score
    team2.GA += team2_score; team2.GF += team1_score