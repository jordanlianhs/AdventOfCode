import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "test.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


"""
Returns a list of tuples containing the surrouding positions of special characters in a file.
"""
positions = []
# We get the indices of the surrounding characters that are special symbols which are not .
for i, line in enumerate(file):
    for j, char in enumerate(line):
        if not char.isalnum() and char != ".":
            positions.append((i, j))

MAX_ROW = len(file)
MAX_COL = len(file[0])


def check_char(i, j, positions):
    """
    Returns True if the current character is adjacent to a special character.
    """
    if (i-1, j-1) in positions or (i-1, j) in positions or (i-1, j+1) in positions or (i, j-1) in positions or (i, j+1) in positions or (i+1, j-1) in positions or (i+1, j) in positions or (i+1, j+1) in positions:
        return True
    else:
        return False


def find_number(j, line):
    original_j = j
    number = line[j]
    if j-1 >= 0 and line[j-1].isnumeric():
        while j-1 >= 0 and line[j-1].isnumeric():
            number = line[j-1] + number
            j -= 1
    j = original_j
    if j+1 <= MAX_COL and line[j+1].isnumeric():
        while j+1 <= MAX_COL-1 and line[j+1].isnumeric():
            number = number + line[j+1]
            j += 1
    return number


result = 0
recent = []
for i, line in enumerate(file):
    for j, char in enumerate(line):
        if check_char(i, j, positions) and char.isnumeric():
            # print(char)
            # print(i,j)
            # print(MAX_COL)
            number = int(find_number(j, line))
            if len(recent) == 0 or recent[-1] != number:
                recent.append(number)
            result += number
print(recent)
print(sum(recent))
print(result)
