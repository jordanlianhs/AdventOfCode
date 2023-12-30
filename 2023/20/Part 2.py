import os
from collections import deque
import math 

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day20.txt")

# Now open the file
try:
    file = open(file_path)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

# name, type, outputs
class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs
        
        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return f"{self.name} type={self.type}, outputs={self.outputs}, memory={self.memory}"

modules = {}
broadcast_targets = []

for line in file:
    left, right= line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, outputs)

# print(broadcast_targets)
# print(modules)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"

# print(modules)

(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

# print(cycle_lengths)
# exit()

presses = 0
while True:
    presses += 1
    # origin, target, pulse
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()
        
        if target not in modules:
            continue

        module = modules[target]

        if module.name == feed and pulse == "hi":
            seen[origin] += 1

            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
            else:
                assert presses == seen[origin] * cycle_lengths[origin]
            
            if all(seen.values()):
                x = 1 
                for cycle_length in cycle_lengths.values():
                    x = math.lcm(x, cycle_length)
                print(x)
                print(seen)
                print(cycle_lengths)
                exit(0)
            
        if module.type == "%":
            if pulse == "lo":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for x in module.outputs:
                q.append((module.name, x, outgoing))
