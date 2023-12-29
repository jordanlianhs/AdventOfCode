import os
from heapq import heappop, heappush

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day17.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

grid = [list(map(int,line.strip())) for line in file]
# print(grid)

seen = set()
# Heatloss, row, column, 
# change in row, change in column, number of times moved in direction
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)

    if r == len(grid)-1 and c == len(grid[0])-1:
        print(hl)
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))

    if n < 3 and (dr,dc) != (0,0):
        nextr, nextc = r + dr, c + dc
        if 0 <= nextr < len(grid) and 0 <= nextc < len(grid[0]):
            heappush(pq, (hl + grid[nextr][nextc], nextr, nextc, dr, dc, n+1))
    
    for nextdirectionr, nextdirectionc in [(0,1), (0,-1), (1,0), (-1,0)]:
        if (nextdirectionr, nextdirectionc) != (dr, dc) and (nextdirectionr, nextdirectionc) != (-dr, -dc): 
            nextr, nextc = r + nextdirectionr, c + nextdirectionc
            if 0 <= nextr < len(grid) and 0 <= nextc < len(grid[0]):
                heappush(pq, (hl + grid[nextr][nextc], nextr, nextc, nextdirectionr, nextdirectionc, 1))