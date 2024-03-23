from club import Club
from fixtures import generate_fixtures
from simulator import simulate_fixture
from league import League
import json
from player import Player, generate_csv_data, ALL_PLAYERS

# generate 18 random teams with different ratings
Avila = Club(_id=1, name="Avilla F.C", rating=78)
BocaJuniors = Club(_id=2, name="Boca Juniors F.C", rating=84)
Bragantino = Club(_id=3, name="Bragantino F.C", rating=72)
Chelsea = Club(_id=4, name="Chelsea F.C", rating=86)
CrystalPalace = Club(_id=5, name="Crystal Palace F.C", rating=78)
FCBarcelona = Club(_id=6, name="FC Barcelona", rating=88)
RealMadrid = Club(_id=7, name="Real Madrid F.C", rating=94)
SevillaFC = Club(_id=8, name="Sevilla F.C", rating=88)
ManCity = Club(_id=9, name="Manchaster City F.C", rating=92)
BayerLevekusen = Club(_id=10, name="Bayer Levekusen F.C", rating=89)
AlNassr = Club(_id=11, name="Al Nassr F.C", rating=87)
ManUtd = Club(_id=12, name="Manchaster Utd F.C", rating=84)
Juventus = Club(_id=13, name="Juventus F.C", rating=86)
SSNapoli = Club(_id=14, name="SSNapoli F.C", rating=89)
PSG = Club(_id=15, name="PSG F.C", rating=87)
Benfica = Club(_id=16, name="Benfica F.C", rating=83)
Bayern = Club(_id=17, name="Bayern F.C", rating=85)
Liverpool = Club(_id=18, name="Liverpool F.C", rating=91)

ALL_CLUBS = [Avila, BocaJuniors, Bragantino, Chelsea, CrystalPalace, 
    FCBarcelona, RealMadrid, SevillaFC, ManCity, BayerLevekusen, AlNassr,
    ManUtd, Juventus, SSNapoli, PSG, Benfica, Bayern, Liverpool]

# generating all players
fixtures = generate_fixtures(ALL_CLUBS)

ALL_RESULTS = []
for fixture in fixtures:
    res = simulate_fixture(*fixture)
    res2 = simulate_fixture(*fixture)
    ALL_RESULTS.append(res)
    ALL_RESULTS.append(res2)

for team in ALL_CLUBS:
    team.generate_league_stats()

LegendsLeague = League("Legends League", ALL_CLUBS)

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

generate_csv_data()
ALL_PLAYERS = ALL_PLAYERS