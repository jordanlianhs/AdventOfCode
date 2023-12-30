import os
from collections import deque

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day22.txt")

# Now open the file
try:
    file = open(file_path)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

bricks = [list(map(int, line.replace("~", ",").split(","))) for line in file]
print(bricks)
# Sort by the z coordinate
bricks.sort(key=lambda brick: brick[2])
print(bricks)

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
    
bricks.sort(key=lambda brick: brick[2])

k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(bricks)):
    if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
        total += 1

print(total)