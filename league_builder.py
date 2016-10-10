import csv

# Read the CSV and get a Python dictionary back
def open_csv(file_name):
	with open(file_name) as file:
		player_reader = csv.DictReader(file, delimiter=',')
	return player_reader
		
		
if __name__ == '__main__':
	open_csv('soccer_players.csv')

# Break the players into two different lists depending if they have previous experience


# Reference a list of teams and assign players to teams.


