import os
import sympy

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day24.txt")

# Now open the file
try:
    file = open(file_path)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in file]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
    if len(answers) == 1:
        break
    
answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])
print(i)