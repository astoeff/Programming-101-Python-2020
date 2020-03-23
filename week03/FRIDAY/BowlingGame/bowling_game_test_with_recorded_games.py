import json
from solution import BowlingGame, Frame
 
class Payload:
	 def __init__(self, j):
		 self.__dict__ = json.loads(j)
 
def main():
	with open("bowling_games_recorded.txt","r") as file:

		line_number = 1
		mistakes = 0
		for line in file:  
			p = Payload(line)
			game = BowlingGame(p.shots)
			if game.calculate_game_score() != p.score:
				print('Wrong calculation on line {n}:'.format(n=line_number))
				print(p.shots, ' ', p.score)
				print('Calculated: ',game.calculate_game_score())
				mistakes += 1
			line_number += 1
		if mistakes == 0:
			print('All {n} games are correctly calculated!'.format(n=line_number-1))

if __name__ == '__main__':
	main()


