from club import Club
from fixtures import generate_fixtures
from simulator import simulate_fixture
from league import League
import json

# generate 18 random teams with different ratings
Avila = Club(1, "Avilla F.C", 78)
BocaJuniors = Club(2, "Boca Juniors F.C", 84)
Bragantino = Club(3, "Bragantino F.C", 72)
Chelsea = Club(4, "Chelsea F.C", 86)
CrystalPalace = Club(5, "Crystal Palace F.C", 78)
FCBarcelona = Club(6, "FC Barcelona", 88)
RealMadrid = Club(7, "Real Madrid F.C", 94)
SevillaFC = Club(8, "Sevilla F.C", 88)
ManCity = Club(9, "Man City F.C", 92)
BayerLevekusen = Club(10, "Bayer Levekusen F.C", 89)
AlNassr = Club(11, "Al Nassr F.C", 87)
ManUtd = Club(12, "Man Utd F.C", 84)
Juventus = Club(13, "Juventus F.C", 86)
SSNapoli = Club(14, "SSNapoli F.C", 89)
PSG = Club(15, "PSG F.C", 87)
Benfica = Club(16, "Benfica F.C", 83)
Bayern = Club(17, "Bayern F.C", 85)
Liverpool = Club(18, "Liverpool F.C", 91)

ALL_CLUBS = [Avila, BocaJuniors, Bragantino, Chelsea, CrystalPalace, 
    FCBarcelona, RealMadrid, SevillaFC, ManCity, BayerLevekusen, AlNassr,
    ManUtd, Juventus, SSNapoli, PSG, Benfica, Bayern, Liverpool]

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
