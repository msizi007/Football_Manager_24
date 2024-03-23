
class Club:
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating
        self.avg = self.rating
        self.P = 0
        self.W = 0
        self.L = 0
        self.D = 0
        self.GA = 0
        self.GF = 0
        self.GD = 0
        self.PTS = 0

    def generate_league_stats(self):
        self.GD = self.GA - self.GF
        self.PTS = (self.W*3) + self.D