
class Club:
    def __init__(self, _id, name: str):
        self._id = _id
        self.name = name
        self.avg = 0
        self.P = 0
        self.W = 0
        self.L = 0
        self.D = 0
        self.GA = 0
        self.GF = 0
        self.GD = 0
        self.PTS = 0
        self.league = None
        self.league_pos = 0
        self.squad = []

        self.W_rate = 0
        self.D_rate = 0
        self.L_rate = 0
        self.GA_rate = 0
        self.GF_rate = 0
        self.GD_rate = 0
        self.PTS_rate = 0

    def generate_league_stats(self):
        self.GD = self.GA - self.GF
        self.PTS = (self.W*3) + self.D

    def add_player(self, player):
        self.squad.append(player)
        player.club = self

    def set_avarage(self):
        total = 0
        for i in range(11):
            total += self.squad[i].avg
        self.avg = int(total/11)

    def generate_rates(self):
        self.W_rate = self.W/self.P
        self.D_rate = self.D/self.P
        self.L_rate = self.L/self.P
        self.GA_rate = self.GA/self.P
        self.GF_rate = self.GF/self.P
        self.GD_rate = self.GD/self.P
        self.PTS_rate = self.PTS/self.P