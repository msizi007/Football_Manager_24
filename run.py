# from main import app
from club import Club
from league import League
import random, math
import itertools
from simulator import simulate_fixture

# generate 18 random teams with different ratings
Avila = Club("Avilla F.C", 78)
BocaJuniors = Club("Boca Juniors F.C", 84)
Bragantino = Club("Bragantino F.C", 72)
Chelsea = Club("Chelsea F.C", 86)
CrystalPalace = Club("Crystal Palace F.C", 78)
FCBarcelona = Club("FC Barcelona", 88)
RealMadrid = Club("Real Madrid F.C", 94)
SevillaFC = Club("Sevilla F.C", 88)
ManCity = Club("Man City F.C", 92)
BayerLevekusen = Club("Bayer Levekusen F.C", 89)
AlNassr = Club("Al Nassr F.C", 87)
ManUtd = Club("Man Utd F.C", 84)
Juventus = Club("Juventus F.C", 86)
SSNapoli = Club("SSNapoli F.C", 89)
PSG = Club("PSG F.C", 87)
Benfica = Club("Benfica F.C", 83)
Bayern = Club("Bayern F.C", 85)
Liverpool = Club("Liverpool F.C", 91)

ALL_CLUBS = [Avila, BocaJuniors, Bragantino, Chelsea, CrystalPalace, 
    FCBarcelona, RealMadrid, SevillaFC, ManCity, BayerLevekusen, AlNassr,
    ManUtd, Juventus, SSNapoli, PSG, Benfica, Bayern, Liverpool]

def generate_fixtures(teams):
    fixtures = []
    
    # Ensure even number of teams
    if len(teams) % 2 != 0:
        teams.append(None)
    
    # Generate home and away matches
    for i in range(len(teams)-1):
        home = teams[:len(teams)//2]
        away = teams[len(teams)//2:][::-1]
        
        round_fixtures = [(home[j], away[j]) for j in range(len(home))]
        fixtures.extend(round_fixtures)
        
        # Rotate teams for the next round
        teams.insert(1, teams.pop())
        
    # Remove fixtures with None (if added)
    fixtures = [(team1, team2) for team1, team2 in fixtures if team1 is not None and team2 is not None]
    
    return fixtures


fixtures = generate_fixtures(ALL_CLUBS)

for fixture in fixtures:
    simulate_fixture(*fixture)
    simulate_fixture(*fixture)

for team in ALL_CLUBS:
    team.generate_league_stats()

LegendsLeague = League("Legends League", ALL_CLUBS)
LegendsLeague.display_table()
# print(RealMadrid.__dict__)



# if __name__ == "__main__":
#     app.run(debug=True)
