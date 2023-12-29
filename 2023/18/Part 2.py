import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day18.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

points = [(0,0)]
directions = {
    "U": (0,1),
    "D": (0,-1),
    "R": (1,0),
    "L": (-1,0)
}
boundarypoints = 0

for line in file:
    _, _, x = line.split()
    x = x[2:-1]
    dr, dc = directions[ "RDLU"[int(x[-1])] ]
    steps = int(x[:-1], 16)
    boundarypoints += steps
    r, c = points[-1]
    points.append((r + dr*steps, c + dc*steps))
print(points)
print(len(points))

# Shoelace formula
# Absolute of Summation of (xi * (yi+1 - yi-1)) / 2
# Since the array points rests on the middle of the grid,
# this formula gets the interior polygon area and half of the boundary points
area = abs(sum(points[i][0] * (points[(i+1) % len(points)][1] - points[i-1][1]) for i in range(len(points))))//2
print(area)

# Pick's theorem
# A = I + B/2 - 1
# This gets the interior polygon area
print(boundarypoints)
i = area - boundarypoints//2 + 1
print(i) # This is the interior polygon area
ans = i + boundarypoints
print(ans)
