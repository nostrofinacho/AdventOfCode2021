# Advent of Code
# ~~~~~ Quantum Die Universe Splitting Extravaganza ~~~~~

from functools import cache

# Input parsing
with open("Day#21_Puzzle#2_Input.txt") as input_data:
    player_positions = tuple(map(int, input_data.read().split()[4:10:5]))


@cache
# Recursive universe to multiverse adapter
def split_the_verse(positions, scores, on_turn):
    # Count the players' wins
    ws_a, ws_b = 0, 0

    # Check the win condition -> only one wins in one paralel verse
    if scores[0] >= 21:
        return 1, 0
    elif scores[1] >= 21:
        return 0, 1

    # Multiverse creation
    for first_roll in (1, 2, 3):
        for second_roll in (1, 2, 3):
            for third_roll in (1, 2, 3):
                # The roll score is the sum of the three rolls
                turn_score = sum((first_roll, second_roll, third_roll))

                # Who's turn was it?
                if on_turn == 0:
                    positions_ = ((positions[0] + turn_score - 1) % 10 + 1, positions[1])
                    scores_ = (scores[0] + positions_[0], scores[1])
                    novaverse = split_the_verse(positions_, scores_, 1)
                else:
                    positions_ = (positions[0], (positions[1] + turn_score - 1) % 10 + 1)
                    scores_ = (scores[0], scores[1] + positions_[1])
                    novaverse = split_the_verse(positions_, scores_, 0)

                # Remember the winners
                ws_a += novaverse[0]
                ws_b += novaverse[1]
    # Return total win counts covered by this universe
    return ws_a, ws_b


# Task solution
game = split_the_verse(player_positions, (0, 0), 0)
print("Wins\n-----\nPlayer 1:", game[0], "\nPlayer 2:", game[1])
print("-----\nTask solution:", max(game))
