
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