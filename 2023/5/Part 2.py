import os
import time

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day5.txt")

# Now open the file
try:
    file = open(file_path).read().strip().split("\n")
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")


seeds = []
seeds.extend(file[0][file[0].find(":")+1:].strip().split(" "))


i = 1
seed_to_soil = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "seed-to-soil map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        seed_to_soil.add((int(source), int(destination), int(length)))


soil_to_fertilizer = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "soil-to-fertilizer map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        soil_to_fertilizer.add((int(source), int(destination), int(length)))

fertilizer_to_water = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "fertilizer-to-water map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        fertilizer_to_water.add((int(source), int(destination), int(length)))

water_to_light = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "water-to-light map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        water_to_light.add((int(source), int(destination), int(length)))

light_to_temp = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "light-to-temperature map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        light_to_temp.add((int(source), int(destination), int(length)))

temp_to_humidity = set()
stop = False
map = False
while not stop:
    i += 1
    if (file[i] == "temperature-to-humidity map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        temp_to_humidity.add((int(source), int(destination), int(length)))

humidity_to_location = set()
stop = False
map = False
while not stop:
    if i < len(file)-1:
        i += 1
    else:
        break
    if (file[i] == "humidity-to-location map:"):
        map = True
        continue
    if file[i] == "":
        stop = True
        break
    if map:
        line = file[i].strip().split(" ")
        length = line[2]
        source = line[1]
        destination = line[0]
        humidity_to_location.add((int(source), int(destination), int(length)))

t0 = time.time()
final_loc = []
for i in range(0,len(seeds),2):
    loc = []
    for j in range(int(seeds[i+1])):
        seed = int(seeds[i])+j
        # print("Seed: ", seed)

        mapped = False
        for source, destination, length in seed_to_soil:
            if source <= seed <= source+length-1:
                soil = destination + seed - source
                mapped = True
        if not mapped:
            soil = seed
        # print(soil)

        mapped = False
        for source, destination, length in soil_to_fertilizer:
            if source <= soil <= source+length-1:
                fertilizer = destination + soil - source
                mapped = True
        if not mapped:
            fertilizer = soil
        # print(fertilizer)

        mapped = False
        for source, destination, length in fertilizer_to_water:
            if source <= fertilizer <= source+length-1:
                water = destination + fertilizer - source
                mapped = True
        if not mapped:
            water = fertilizer
        # print(water)

        mapped = False
        for source, destination, length in water_to_light:
            if source <= water <= source+length-1:
                light = destination + water - source
                mapped = True
        if not mapped:
            light = water
        # print(light)

        mapped = False
        for source, destination, length in light_to_temp:
            if source <= light <= source+length-1:
                temp = destination + light - source
                mapped = True
        if not mapped:
            temp = light
        # print(temp)

        mapped = False
        for source, destination, length in temp_to_humidity:
            if source <= temp <= source+length-1:
                humidity = destination + temp - source
                mapped = True
        if not mapped:
            humidity = temp
        # print(humidity)

        mapped = False
        for source, destination, length in humidity_to_location:
            if source <= humidity <= source+length-1:
                location = destination + humidity - source
                mapped = True
        if not mapped:
            location = humidity
        loc.append(location)
    t1 = time.time()
    print(t1-t0)
    final_loc.append(min(loc))
    

print(final_loc)
print(min(final_loc))
