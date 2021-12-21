# Advent of Code
# ~~~~~ The Non-gamblers Roulette ~~~~~

# The dice that rolls 1,2,3,4,...,99,100,1,2,3,...,99,100,1,2,.....
class DeterministicDice:
    def __init__(self):
        self.last_roll = 0

    # He's checking it once
    def roll(self):
        self.last_roll += 1
        if self.last_roll == 100:
            self.last_roll = 0
        return self.last_roll

    # He's checking it thrice
    def roll_thrice(self):
        return self.roll(), self.roll(), self.roll()


# Wicked
class Game:
    # The playing order is the order in which the players' names are given
    def __init__(self, player_names, boardsize, dice):
        self.players = player_names
        self.number_of_players = len(player_names)
        self.scores = dict.fromkeys(player_names, 0)
        self.positions = dict.fromkeys(player_names, 1)
        self.boardsize = 10
        self.dice = dice
        self.dice_rolls = 0

    def play(self):
        state_cnt = 0

        # Print starting state
        print("-" * 30, "\nGamestate #", str(state_cnt))
        self.print_state()

        # Gameloop
        while True:
            player = self.players[state_cnt % self.number_of_players]
            turn_score = sum(self.dice.roll_thrice())
            self.dice_rolls += 3
            self.positions[player] = (self.positions[player] + turn_score - 1) % self.boardsize + 1
            self.scores[player] += self.positions[player]
            state_cnt += 1

            # Printout
            print("-"*30, "\nGamestate #", str(state_cnt))
            self.print_state()

            # Check the scores
            for player in self.players:
                if self.scores[player] >= 1000:
                    print("", "-"*11, "\n |Game Over|\n", "-"*11)
                    # Return winner, and losers
                    return player, [p for p in self.players if p != player]

    # Prints the current game info
    def print_state(self):
        print("Players:", self.players)
        print("Positions:", self.positions)
        print("Scores:", self.scores)


# Input parsing
with open("Day#21_Puzzle#1_Input.txt") as input_data:
    player1_position, player2_position = list(map(int, input_data.read().replace("\n", " ")[:-1].split(" ")[4:10:5]))
    player1_score, player2_score = 0, 0

# Prepare the game
game = Game(['Santa Claus', 'Mrs. Claus'], 10, DeterministicDice())
game.positions['Santa Claus'] = player1_position
game.positions['Mrs. Claus'] = player2_position

# Play the game
winner, losers = game.play()

# Task solution
print("Losing player's score multiplied by number of times the die has been rolled:", game.scores[losers[0]] * game.dice_rolls)
