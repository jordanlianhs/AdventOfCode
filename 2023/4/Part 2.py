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


cards = {i+1:1 for i in range(len(file)) }

for line in file:
    card = cards[int(line[4:line.find(":")].strip())]
    copy = 0

    winning_list = []
    matching_list = []
    winning_list.extend(line[line.find(":")+1:line.find("|")-1].strip().split(" "))
    matching_list.extend(line[line.find("|")+1:].strip().split(" "))
    while "" in winning_list:
        winning_list.remove("")
    while "" in matching_list:
        matching_list.remove("")
    for i in winning_list:
        if i in matching_list:
            copy += 1
    for i in range(copy):
        cards[int(line[4:line.find(":")].strip())+i+1] += cards[int(line[4:line.find(":")].strip())]

print(cards)
print(sum(cards.values()))

# {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
# {1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1}
# {1: 1, 2: 2, 3: 4, 4: 4, 5: 2, 6: 1}
# {1: 1, 2: 2, 3: 4, 4: 8, 5: 6, 6: 1}
# {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}