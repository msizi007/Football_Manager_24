from club import Club
from fixtures import generate_fixtures
from simulator import simulate_fixture
from league import League

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

fixtures = generate_fixtures(ALL_CLUBS)

for fixture in fixtures:
    simulate_fixture(*fixture)
    simulate_fixture(*fixture)

for team in ALL_CLUBS:
    team.generate_league_stats()

LegendsLeague = League("Legends League", ALL_CLUBS)