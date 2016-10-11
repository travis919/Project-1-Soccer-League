import csv

# Read the CSV and get a Python dictionary back
def open_csv(file_name):
	'''Opens the CSV file, transforms it's contents into a list of dictionary objects, and returns the list'''
	with open(file_name) as file:
		player_dict = list(csv.DictReader(file, delimiter=','))
	return player_dict

def assigner(teams, players):
	'''Takes a list of available teams, and a list of dicts. Adds a "Team" attribute to each dict and ensures teams assigned are even'''
	count = 1
	for player in players:
		if count == 1:
			player["Team"] = teams[0]
			count += 1
		elif count == 2:
			player["Team"] = teams[1]
			count += 1
		else:
			player["Team"] = teams[2]
			count = 1



def build_teams(player_dict):
	'''Sorts players into experienced and inexperienced players'''
	experienced_players = []
	noobs = []
	teams = ["Sharks", "Dragons", "Raptors"]
	for player in player_dict:
		if player["Soccer Experience"] == "YES":
			experienced_players.append(player)
		else:
			noobs.append(player)
	assigner(teams, experienced_players)
	assigner(teams, noobs)

	return experienced_players, noobs


def generate_letters(players):
	'''Takes in a list of dicts and generates personalized letters for each player. Letter is addressed to players parents and includes their assigned team and data/time of first practice'''
	for player in players:
		name_split = player["Name"].lower().split()
		name_join = "_".join(name_split)
		file = open("{}.txt".format(name_join), "w")
		practice_time = ""
		if player["Team"] == "Raptors":
			practice_time = "March 18, 1PM"
		elif player["Team"] == "Sharks":
			practice_time = "March 17, 3PM"
		else:
			practice_time = "March 17, 1PM"
		file.write("""
Dear {Guardian Name(s)},
Your child has been selected to participate in our Quidditch league! {Name} will be playing on the {Team} team. The team's first practice will be on {Practice}.
Please refer to our sport as 'Soccer' in public to avoid issues with muggles. Thank you.
Yours sincerely,
	Travis
			""".format(Practice = practice_time, **player))

		
if __name__ == '__main__':
	players = open_csv('soccer_players.csv')
	players_experienced, players_new = build_teams(players)
	generate_letters(players_experienced)
	generate_letters(players_new)
