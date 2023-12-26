import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day14.txt")

# Now open the file
try:
    grid = tuple(open(file_path).read().strip().split())
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join("".join(sorted(tuple(group), reverse=True))for group in row.split("#")) for row in grid)
        grid = tuple(row[::-1] for row in grid)

seen = {grid}
array = [grid]
iter = 0
while True:
    iter +=1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)
# print(iter, first)
grid = array[(1000000000 - first) % (iter - first) + first]

print(sum(row.count("O") * (len(grid) -r) for r,row in enumerate(grid)))