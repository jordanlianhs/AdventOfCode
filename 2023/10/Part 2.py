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

loop = {(start_row, start_col)}
queue = deque([(start_row, start_col)])
# Finding out what the S is
maybe_s = {"|", "-", "7", "J", "L", "F"}

while queue:
    r, c = queue.popleft()
    ch = grid[r][c]

    # In order to go up
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r-1, c) not in loop:
        loop.add((r-1, c))
        queue.append((r-1, c))
        if ch == "S":
            # If it's the start, then it can be the intersection of current set and the following three
            maybe_s &= {"|", "J", "L"}
    # In order to go down
    if r < len(grid)-1 and ch in "S|7F" and grid[r+1][c] in "|JL" and (r+1, c) not in loop:
        loop.add((r+1, c))
        queue.append((r+1, c))
        if ch == "S":
            # If it's the start, then it can be the intersection of current set and the following three
            maybe_s &= {"|", "7", "F"}
    # In order to go left
    if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r, c-1) not in loop:
        loop.add((r, c-1))
        queue.append((r, c-1))
        if ch == "S":
            # If it's the start, then it can be the intersection of current set and the following three
            maybe_s &= {"-", "J", "7"}
    # In order to go right
    if c < len(row)-1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in loop:
        loop.add((r, c+1))
        queue.append((r, c+1))
        if ch == "S":
            # If it's the start, then it can be the intersection of current set and the following three
            maybe_s &= {"-", "L", "F"}

assert len(maybe_s) == 1
(S,) = maybe_s
# print(S)

# Now we have the S, we can replace S in the grid with the supposed character
grid = [row.replace("S", S) for row in grid]
# Replace characters that are not in a loop as they do not affect if vertically and horizontally sweep through the grid
grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row))
        for r, row in enumerate(grid)]
# print(grid)
# print("\n".join(grid))


# Horizontal sweep
outside = set()
for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        # There is a crossing of a pipe
        if ch == "|":
            # Should not have an up down if we are riding along a pipe
            assert up is None
            # Flip the within
            within = not within
        # We did hit one of the four special characters
        elif ch == "-":
            # Ride along the pipe
            assert up is not None
        elif ch in "LF":
            # Should not have an up down if we are riding along a pipe
            assert up is None
            # If character is L, we are facing up (True), otherwise it is F and we are facing down (False)
            up = ch == "L"
        elif ch in "J7":
            # Ride along the pipe
            assert up is not None
            # If we are facing up, then we should have a J, otherwise we should have a 7, if not equals to that we flip the within
            if ch != ("J" if up else "7"):
                within = not within
            # Ride past/across the pipe
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"Unknown character horizontal: {ch}")
        if not within:
            outside.add((r, c))


# for r in range(len(grid)):
#     for c in range(len(grid[r])):
#         print("#" if (r, c) in (outside-loop) else ".", end="")
#     print()

print(len(grid) * len(grid[0]) - len(outside | loop))
