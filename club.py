
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

        self.attacking_strength = 0
        self.defense_strength = 0

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

    def generate_strength_rates(self):
        self.attacking_strength = self.league.avg_GF
        self.defense_strength = self.league.avg_GA