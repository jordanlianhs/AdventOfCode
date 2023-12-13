from math import gcd
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day8.txt")

# Now open the file
try:
    steps, _, *rest = open(file_path).read().splitlines()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


network = {}

for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

positions = [key for key in network if key.endswith("A")]
cycles = []

for current in positions:
    cycle = []

    current_steps = steps
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"): # While we haven't reached Z or we're at the start
            step_count += 1
            current = network[current][0 if current_steps[0] == "L" else 1] # Move from current to next
            current_steps = current_steps[1:] + current_steps[0] # Rotate the string

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
        else:
            # We never go into else, suggesting that it goes through if then the elif and breaks, thus one cycle
            assert current!= first_z
            print("Hi")
            step_count = 0

    cycles.append(cycle)

print(cycles) # Note how there is only 2 cycle in each cycles so it goes from the first z to the same z

# We need the LCM of all the cycles since each cycle is just one step
nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)

print(lcm)