import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day15.txt")

# Now open the file
try:
    file = open(file_path).read().strip()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


def hash(s):
    v = 0
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256
    return v
# print(hash("HASH"))
print(sum(map(hash, file.split(","))))
