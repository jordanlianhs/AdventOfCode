import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day19.txt")

# Now open the file
try:
    file = open(file_path).read().strip()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


block1, block2 = file.split("\n\n")

workflows = {}

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    # print(name, rest)
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        comparator = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, comparator, n, target))
print(workflows)
operators = {
    ">": int.__gt__,
    "<": int.__lt__,
}

def accept(item, name = "in"):
    if name == "R":
        return False
    if name == "A":
        return True
    
    rules, fallback = workflows[name]

    for key, comparator, n, target in rules:
        if operators[comparator](item[key], n):
            return accept(item, target)
    
    return accept(item, fallback)

total = 0
for line in block2.splitlines():
    item = {}
    for segment in line[1:-1].split(","):
        char, n = segment.split("=")
        item[char] = int(n)
    print(item)
    if accept(item):
        total += sum(item.values())

print(total)
