import os
from collections import deque

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day10.txt")

# Now open the file
try:
    grid = open(file_path).read().strip().splitlines()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        # print(r, c)
        if ch == "S":
            start_row = r
            start_col = c
            break
    else:
        continue
    break

seen = {(start_row, start_col)}
queue = deque([(start_row, start_col)])

while queue:
    r, c = queue.popleft()
    ch = grid[r][c]

    # In order to go up
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r-1, c) not in seen:
        seen.add((r-1, c))
        queue.append((r-1, c))
    # In order to go down
    if r < len(grid)-1 and ch in "S|7F" and grid[r+1][c] in "|JL" and (r+1, c) not in seen:
        seen.add((r+1, c))
        queue.append((r+1, c))
    # In order to go left
    if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r, c-1) not in seen:
        seen.add((r, c-1))
        queue.append((r, c-1))
    # In order to go right
    if c < len(row)-1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in seen:
        seen.add((r, c+1))
        queue.append((r, c+1))

print(len(seen)//2)
