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
print(hash("qp"))
print(hash("cm"))

boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in file.split(","):
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
        if label in focal_lengths.keys():
            del focal_lengths[label]
    else:
        label, length = instruction.split("=")
        length = int(length)

        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = length

print(boxes)
print(focal_lengths)

total = 0

for box_num, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_num * lens_slot * focal_lengths[label]

print(total)
