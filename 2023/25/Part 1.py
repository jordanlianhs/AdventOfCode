import os
import networkx as nx

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the file
file_path = os.path.join(script_dir, "day25.txt")

# Now open the file
try:
    file = open(file_path)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

g = nx.Graph()

for line in file:
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))