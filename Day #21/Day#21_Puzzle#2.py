# Advent of Code
# ~~~~~ Quantum Die Universe Splitting Extravaganza ~~~~~
import sys
from functools import cache
sys.setrecursionlimit(100000)

# A single gamestate
@cache
class GameState:
    wins = None

    @cache
    # The playing order is the order in which the players' names are given
    def __init__(self, player_names):
        self.players = player_names
        self.number_of_players = len(player_names)
        self.scores = dict.fromkeys(player_names, 0)
        self.positions = dict.fromkeys(player_names, 1)

    @cache
    def play(self, player, rester):
        # Check the scores
        for player in self.players:
            if self.scores[player] >= 21:
                self.wins[player] += 1
                return

        # Who's turn
        for first_roll in (1, 2, 3):
            for second_roll in (1, 2, 3):
                for third_roll in (1, 2, 3):
                    next_gamestate = GameState(self.players)
                    turn_score = sum((first_roll, second_roll, third_roll))
                    next_gamestate.positions[player] = (self.positions[player] + turn_score - 1) % 10 + 1
                    next_gamestate.scores[player] = self.scores[player] + next_gamestate.positions[player]

                    next_gamestate.positions[rester] = self.positions[rester]
                    next_gamestate.scores[rester] = self.positions[rester]

                    next_gamestate.play(rester, player)
        return


# Input parsing
with open("Day#21_Puzzle#2_Input_Example.txt") as input_data:
    player1_position, player2_position = list(map(int, input_data.read().replace("\n", " ")[:-1].split(" ")[4:10:5]))

# Prepare the game
game = GameState(('Santa Claus', 'Mrs. Claus'))
game.positions['Santa Claus'], game.positions['Mrs. Claus'] = player1_position, player2_position
game.wins = dict.fromkeys(['Santa Claus', 'Mrs. Claus'], 0)

# Play the game
game.play('Santa Claus', 'Mrs. Claus')
print(game.wins)
