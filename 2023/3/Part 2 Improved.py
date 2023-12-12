import os
from collections import defaultdict

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day3.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

G = [[c for c in line] for line in file]
R = len(G)
C = len(G[0])

nums = defaultdict(list)
for r in range(R):
    gears = set()  # positions of '*' characters next to the current number
    n = 0
    has_part = False
    for c in range(C + 1):  # Plus one so that we can check the last number at the end of a column
        if c < C and G[r][c].isdigit(): # Keep adding to the number if the current character is a digit
            n = n*10+int(G[r][c])
            for rr in [-1, 0, 1]:      # Check the surrounding characters
                for cc in [-1, 0, 1]:  # Check the surrounding characters
                    if 0 <= r+rr < R and 0 <= c+cc < C:
                        ch = G[r+rr][c+cc]
                        if ch == '*':
                            gears.add((r+rr, c+cc)) # Add the position of the '*' character to the set
        elif n > 0: # If the current character is not a digit, done processing the current number
            for gear in gears:       # If a number has no '*' next to it, then the set will be empty, and the number will not be added to the dictionary
                nums[gear].append(n) # Add the number to the list of numbers at the position of the '*' character
            n = 0
            gears = set()
# print(nums)
p2 = 0
for k, v in nums.items():
    if len(v) == 2:
        p2 += v[0]*v[1]
    else:
        print(k,v)
print(p2)

