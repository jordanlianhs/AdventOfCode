import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day2.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

result = 0
for line in file:
    minimal = {'red': 0, 'green': 0, 'blue': 0}
    games = line[line.find(":")+2:].split("; ")
    for game in games:
        game_set = game.split(", ")
        for cube in game_set:
            if int(cube[:cube.find(" ")]) > minimal[cube[cube.find(" ")+1:]]:
                minimal[cube[cube.find(" ")+1:]] = int(cube[:cube.find(" ")])
    product = 1
    for value in minimal.values():
        product *= value
    result += product


print(result)
