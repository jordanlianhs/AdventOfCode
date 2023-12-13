import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day6.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


times = [int(t) for t in file[0].split(":")[1].strip().split()]
record_dist = [int(dist) for dist in file[1].split(":")[1].strip().split()]
# print(time)
# print(dist)

number_of_ways = [0 for _ in range(len(times))]


dist_final = []
for i, time in enumerate(times):

    dist = []
    for j in range(time+1):
        speed = j
        hold_time = j
        dist_travelled = speed * (time-hold_time)
        dist.append(dist_travelled)
    
    for k in dist:
        if k > record_dist[i]:
            number_of_ways[i] += 1

print(number_of_ways)

result = 1
for i in number_of_ways:
    result *= i
print(result)