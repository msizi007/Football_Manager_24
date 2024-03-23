
class Club:
    def __init__(self, _id, name: str,  rating: int=50):
        self._id = _id
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
        self.league = None
        self.league_pos = 0

    def generate_league_stats(self):
        self.GD = self.GA - self.GF
        self.PTS = (self.W*3) + self.D