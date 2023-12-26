import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "test.txt")

# Now open the file
try:
    grid = open(file_path).read().strip().split()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def print_grid(grid):
    for row in grid:
        print(row)
    print()

grid = list(map("".join, zip(*grid)))
print_grid(grid)

grid = ["#".join("".join(sorted(list(group), reverse=True))
                 for group in row.split("#")) for row in grid]
print_grid(grid)

grid = list(map("".join, zip(*grid)))
print_grid(grid)

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
