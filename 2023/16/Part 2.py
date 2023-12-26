import os
from collections import deque

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day16.txt")

# Now open the file
try:
    grid = open(file_path).read().strip().split()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

ROW = len(grid)
COL = len(grid[0])

def calc(r,c,dr,dc):

    # row, col, delta row, delta col
    a = [(r,c,dr,dc)]
    seen = set()
    q = deque(a)

    while q:
        (r, c, dr, dc) = q.popleft()

        r += dr
        c += dc

        if r < 0 or r>=ROW or c < 0 or c >= COL:
            continue
        
        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r,c,dr,dc) not in seen:
                seen.add((r,c,dr,dc))
                q.append((r,c,dr,dc))
        elif ch == "/":
            # (0,1) -> (-1,0), (1,0) -> (0,-1), (0,-1) -> (1,0), (-1,0) -> (0,1)
            # (dr,dc) -> (-dc,-dr)
            dr, dc = -dc, -dr
            if (r,c,dr,dc) not in seen:
                seen.add((r,c,dr,dc))
                q.append((r,c,dr,dc))
        elif ch == "\\":
            # (0,1) -> (1,0), (1,0) -> (0,1), (0,-1) -> (-1,0), (-1,0) -> (0,-1)
            # (dr,dc) -> (dc,dr)
            dr, dc = dc, dr
            if (r,c,dr,dc) not in seen:
                seen.add((r,c,dr,dc))
                q.append((r,c,dr,dc))
        else:
            for dr, dc in [(1,0), (-1,0)] if ch == "|" else [(0,1), (0,-1)]:
                if (r,c,dr,dc) not in seen:
                    seen.add((r,c,dr,dc))
                    q.append((r,c,dr,dc))

    coords = {(r,c) for (r,c,_,_) in seen}
    return len(coords)

max_val = 0

for r in range(ROW):
    max_val = max(max_val, calc(r,-1,0,1))
    max_val = max(max_val, calc(r,COL,0,-1))

for c in range(COL):
    max_val = max(max_val, calc(-1,c,1,0))
    max_val = max(max_val, calc(ROW,c,-1,0))

print(max_val)