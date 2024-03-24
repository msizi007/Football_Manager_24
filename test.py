import csv

POS = [
    ['CM', 'RW', 'ST', 'CB', 'LW', 'CDM', 'GK', 'CAM', 'LB', 
     'RB', 'LM', 'RM', 'RWB', 'CF', 'LWB']
]

with open("new_players.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    positions = []
    for line in csv_reader:
        if line['Best Position'] not in positions:
            positions.append(line['Best Position'])

    print(positions)