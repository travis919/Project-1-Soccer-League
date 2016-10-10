import csv

# Read the CSV and get a Python dictionary back
def open_csv(file_name):
	with open(file_name) as file:
		player_dict = list(csv.DictReader(file, delimiter=','))
	return player_dict


def build_teams(player_dict):
	experienced_players = []
	noobs = []
	for player in player_dict:
		if player["Soccer Experience"] == "YES":
			experienced_players.append(player)
		else:
			noobs.append(player)
	count = 1
	for player in experienced_players:
		if count == 1:
			player["Team"] = "Sharks"
			count += 1
		elif count == 2:
			player["Team"] = "Dragons"
			count += 1
		else:
			player["Team"] = "Raptors"
			count = 1
	count_2 = 1
	for player in noobs:
		if count_2 == 1:
			player["Team"] = "Sharks"
			count_2 += 1
		elif count_2 == 2:
			player["Team"] = "Dragons"
			count_2 += 1
		else:
			player["Team"] = "Raptors"
			count_2 = 1
	return experienced_players, noobs


def generate_letters(players_experienced, players_new):
	pass

		
if __name__ == '__main__':
	players = open_csv('soccer_players.csv')
	players_experienced, players_new = build_teams(players)

# Break the players into two different lists depending if they have previous experience


# Reference a list of teams and assign players to teams.


