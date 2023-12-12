import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day4.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

points = 0
for line in file:
    winning_list = []
    matching_list = []
    point = 0
    winning_list.extend(line[line.find(":")+1:line.find("|")-1].strip().split(" "))
    matching_list.extend(line[line.find("|")+1:].strip().split(" "))
    while "" in winning_list:
        winning_list.remove("")
    while "" in matching_list:
        matching_list.remove("")
    for i in winning_list:
        if i in matching_list and point == 0:
            point += 1
        elif i in matching_list:
            point *= 2
    points += point
print(points)
