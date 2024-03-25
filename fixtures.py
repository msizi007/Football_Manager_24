
def generate_fixtures(teams):
    fixtures = []
    
    # # Ensure even number of teams
    # if len(teams) % 2 != 0:
    #     teams.append(None)
    
    # Generate home and away matches
    for i in range(len(teams)):
        for j in range(len(teams)):

            if i != j:
                home_team = teams[i]
                away_team = teams[j]

                fixture = (home_team, away_team)
                fixtures.append(fixture)

    # Remove fixtures with None (if added)
    fixtures = [(team1, team2) for team1, team2 in fixtures if team1 is not None and team2 is not None]
    
    return fixtures