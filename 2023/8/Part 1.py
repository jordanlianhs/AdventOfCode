import os
from collections import defaultdict
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day8.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

instructions = file[0]
camelmap = defaultdict(str, {line.split("=")[0].strip(): (line.split("=")[1].strip()[1:4], line.split("=")[1].strip()[6:9]) for line in file[2:]})
# print(instructions)
# print(camelmap)

final_instructions = []
final_instructions.append(instructions)
state = "AAA"
# print(state)
steps = 0
while state != "ZZZ":
    instruction = final_instructions.pop()
    for i in instruction:
        if i == "R":
            move = camelmap[state][1]
        elif i == "L":
            move = camelmap[state][0]
        state = move
    steps += len(instruction)
    if state != "ZZZ":
        final_instructions.append(instruction)
print(steps)
