import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day1.txt")

# Now open the file
try:
    file = open(file_path, "r")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

result = 0

for line in file.readlines():
    for char in line:
        if char.isalpha() or char.isspace():
            line = line.replace(char, "")
    digits = int(line)
    if len(line) == 1:
        result += int(digits) * 11
    else:
        result += int(line[0]) *10 +  int(line[-1:])


print(result)
