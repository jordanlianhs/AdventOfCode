import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day9.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

result = []

for line in file:
    seq = [int(x) for x in line.split(" ")]
    last_elements = []
    while (not all(x == 0 for x in seq)):
        last_elements.append(seq[0])
        for i in range(len(seq)-1):
            seq[i] = seq[i+1] - seq[i]
        seq.pop()
    print(*last_elements)

    actual = 0
    for i in range(len(last_elements)-1,-1,-1):
        # print(i)
        actual = last_elements[i] - actual
    result.append(actual)

print(sum(result))
