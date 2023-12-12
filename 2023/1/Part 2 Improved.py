import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day1.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


result = 0

for line in file:
    # print(line)
    result_digits = []
    for index, char in enumerate(line):
        if char.isdigit():
            result_digits.append(char)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[index:].startswith(val):
                result_digits.append(str(d + 1))
    # print(result_digits)
    result += int(result_digits[0]+result_digits[-1])

print(result)
