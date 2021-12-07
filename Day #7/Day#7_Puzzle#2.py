# Advent of Code 2021
# The first puzzle of the seventh day
# ~~~~~ The Treachery of Whales ~~~~~
# Finding the optimal crab shuffle (the one that uses up the least amount of fuel)
# This time the crabean submarines don't burn fuel at a constant rate

from scipy.optimize import minimize_scalar

# Initial positions of crabean submarines
crab_positions = None


# Calculates the total cost for all the crabs to move to the destination
def total_cost(destination):
    global crab_positions
    sum41 = 0
    for p in crab_positions:
        for i in range(round(abs(destination - p)+1)):
            sum41 += i
    return sum41


# Reading the crab intel
with open("Day#7_Puzzle#2_Input.txt") as f:
    crab_positions = sorted(list(map(int, f.readline().strip().split(","))))

# The position which should be optimal
optimal_position = minimize_scalar(total_cost)["x"]
print("Optimal final destination:", optimal_position, "-->", round(optimal_position))

# The total final cost
final_cost = total_cost(round(optimal_position))
print("Total fuel consumption:", final_cost)

# Compare it with the simpler solution
optimal_position_simple = sum(crab_positions)/len(crab_positions)
# Check for imperfections
optimal_position_simple = optimal_position_simple - 1 if total_cost(optimal_position_simple - 1) < total_cost(optimal_position_simple) else optimal_position_simple
optimal_position_simple = optimal_position_simple + 1 if total_cost(optimal_position_simple + 1) < total_cost(optimal_position_simple) else optimal_position_simple
print("\nOptimal final destination (simple)", optimal_position_simple, "-->", round(optimal_position_simple))

# The total final cost for the simpler solution
final_cost_simple = total_cost(round(optimal_position_simple))
print("Total fuel consumption (simple):", final_cost_simple)
