import csv

ALL_PLAYERS = []

class Player:
    def __init__(self, _id, known_as, fullname, avg, age, potential, value,  position, secondary_positions,
        club, nationality, image_link, wage, release_clause, contract_until, joined_on, national_team_name):
        self._id = _id
        self.known_as = known_as
        self.fullname = fullname
        self.avg = avg
        self.age = age
        self.potential = potential
        self.value = value
        self.position = position
        self.secondary_positions = secondary_positions
        self.club = club
        self.nationality = nationality
        self.image_link = image_link
        self.wage = wage
        self.release_clause = release_clause
        self.contract_until = contract_until
        self.joined_on = joined_on
        self.national_team_name = national_team_name

        self.P = 0
        self.G = 0
        self.A = 0
        self.form = 0

        # add playe to list of players
        ALL_PLAYERS.append(self)

FINAL_DATA = []
ALL_FIELDNAMES = []
UNWANTED_FIELDNAMES = []
HEADERS = ['Known As', 'Full Name', 'Overall', 'Age', 'Potential', 'Value(in Euro)', 'Positions Played',
            'Best Position', 'Nationality', 'Image Link', 'Club Name', 'Wage(in Euro)', 'Release Clause',
            'Contract Until', 'Joined On', 'National Team Name']

def generate_players_csv_data(ALL_CLUBS):
    # read csv and get all fieldnames
    with open("players.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        ALL_FIELDNAMES = [key for key in csv_reader.fieldnames]
    
        # add all players with corresponding clubs to final data
        for line in csv_reader:
            if line['Club Name'] in [club.name for club in ALL_CLUBS]:
                FINAL_DATA.append(line)

        # open the new csv file and write the headers
        with open("new_players.csv", "w") as outfile:
            csv_writer = csv.DictWriter(outfile, fieldnames=HEADERS)
            csv_writer.writeheader()

            # check for all other fields that were not inclided in headers and remove them..
            unwanted_fields = [field for field in ALL_FIELDNAMES if field not in HEADERS]
            for line in FINAL_DATA:
                for field in unwanted_fields:
                    del line[field]
            
            csv_writer.writerows(FINAL_DATA)

        generate_players()

    # add player to their respective clubs
    for player in ALL_PLAYERS:
        for club in ALL_CLUBS:
            if player.club == club.name:
                club.add_player(player)

    # calculate club avarage for each club
    for club in ALL_CLUBS:
        club.set_avarage()

def generate_players():
    for _id, player in enumerate(FINAL_DATA, start=1):
        player_obj = Player(_id=int(_id), known_as=player['Known As'], fullname=player['Full Name'], avg=int(player['Overall']), age=int(player['Age']),
            potential=int(player['Potential']), value=player['Value(in Euro)'], secondary_positions=player['Positions Played'], 
            position=player['Best Position'], nationality=player['Nationality'], image_link=player['Image Link'], club=player['Club Name'],
            wage=player['Wage(in Euro)'], release_clause=player['Release Clause'], contract_until=player['Contract Until'],
            joined_on=player['Joined On'], national_team_name=player['National Team Name'])
        ALL_PLAYERS.append(player_obj)

    
                    