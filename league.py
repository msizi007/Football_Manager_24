from tabulate import tabulate
class League:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
        self.avg_rating = self.calc_avarage_rating()

        # set every club's league to this league
        for team in self.teams:
            team.league = self

    def calc_avarage_rating(self):
        total = 0
        for team in self.teams:
            total += team.avg
        self.avg_rating = total / len(self.teams)

    def order_table(self):
        self.teams.sort(key=lambda x: x.avg, reverse=True)

    def display_table(self):
        self.order_table()
        headers = ['Name', 'P', 'W', 'D', 'L', 'GA', 'GF', 'GD', 'PTS']
        data = []
        for team in self.teams:
            data.append([team.name, team.P, team.W, 
                team.D, team.L, team.GA, team.GF, 
                team.GD, team.PTS])
        print(tabulate(data, headers=headers, tablefmt="grid"))
            

        