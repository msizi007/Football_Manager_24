
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

    def generate_league_stats(self):
        self.GD = self.GA - self.GF
        self.PTS = (self.W*3) + self.D

    def add_player(self, player):
        self.squad.append(player)

    def set_avarage(self):
        total = 0
        for player in self.squad:
            total += player.avg

        self.avg = int(total/(len(self.squad)))