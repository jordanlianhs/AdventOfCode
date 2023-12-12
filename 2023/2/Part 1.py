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

limit = {'red': 12, 'green': 13, 'blue': 14}
result = 0
for line in file:
    games = line[line.find(":")+2:].split("; ")
    exceed = False
    for game in games:
        game_set = game.split(", ")
        for cube in game_set:
            if int(cube[:cube.find(" ")]) > limit[cube[cube.find(" ")+1:]]:
                exceed = True
                result += int(line[line.find(" ")+1:line.find(":")])
                break
        if exceed:
            break
n = int(line[line.find(" ")+1:line.find(":")])
total = int(n*(n+1)/2)
result = total - result
print(result)
