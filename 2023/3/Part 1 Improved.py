import os

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

p1 = 0
for r in range(R):
    n = 0
    has_part = False
    for c in range(C + 1):  # Plus one so that we can check the last number at the end of a column
        if c < C and G[r][c].isdigit(): # Keep adding to the number if the current character is a digit
            n = n * 10 + int(G[r][c])  
            for rr in [-1, 0, 1]:      # Check the surrounding characters
                for cc in [-1, 0, 1]:  # Check the surrounding characters
                    if 0 <= r + rr < R and 0 <= c + cc < C: 
                        ch = G[r + rr][c + cc] 
                        if not ch.isdigit() and ch != '.': # If the surrounding character is not a digit or a '.'
                            has_part = True
        elif n > 0:      # If the current character is not a digit, done processing the current number
            if has_part: # If the number has a part next to it
                p1 += n  # Add the number to the total
            n = 0
            has_part = False
print(p1)
