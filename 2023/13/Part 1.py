import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day13.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def find_mirror(grid):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
    return 0
    
total = 0
for block in file:
    grid = block.splitlines()
    # print(grid)

    row = find_mirror(grid)
    total += row * 100

    col = list(zip(*grid))
    col = find_mirror(col)
    total += col
print(total)
