from club import Club
from fixtures import generate_fixtures
from simulator import simulate_fixture
from league import League, PREMIER_LEAGUE_CLUB_NAMES
import json
from player import Player, generate_players_csv_data, ALL_PLAYERS

# CONSTANTS
ALL_CLUBS = []

for _id, club_name in enumerate(PREMIER_LEAGUE_CLUB_NAMES, start=1):
    club_obj = Club(_id=_id, name=club_name)
    ALL_CLUBS.append(club_obj)

# generate and save all players
generate_players_csv_data(ALL_CLUBS)

# CREATE A LEAGUE
PREMIER_LEAGUE = League("Premier League", ALL_CLUBS)

# generating all players
fixtures = generate_fixtures(ALL_CLUBS)

ALL_RESULTS = []
for fixture in fixtures:
    res = simulate_fixture(*fixture)
    ALL_RESULTS.append(res)

for team in ALL_CLUBS:
    team.generate_league_stats()


# LEAGUE STSTS IN A JSON FILE
LEAGUE_ANALYSIS = dict()

def record_league_stats():
    for club in ALL_CLUBS:
        data = {'P': club.P,
            'W': club.W,
            'D': club.D,
            'L': club.L,
            'GA': club.GA,
            'GF': club.GF,
            'GD': club.GD,
            'PTS': club.PTS}
        LEAGUE_ANALYSIS[club.name] = data

record_league_stats()
with open('league_analyses.json', 'w') as file:
    json.dump(LEAGUE_ANALYSIS, file, indent=4)