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


block1, _ = file.split("\n\n")

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

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0
    for key, comparator, n, target in rules:
        lo, hi = ranges[key]
        if comparator == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
    return total

print(count({key: (1,4000) for key in "xmas"}))