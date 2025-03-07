import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree

"""
A = Animation
Ac = Action 
An = Anime 
B = Biographical 
C = Comedy 
Cr = Crime 
D = Drama 
Do = Documentary 
F = Fantasy 
H = Historical 
Ho - Horror 
M = Musical 
My = Mystery 
R = Romance 
S = Satire
Sc = Sci Fi  
Sp = Sports
T = Thriller 
W = Western 
Z = Zombie 
"""
G = nx.Graph() # create a new Graph

G.add_edge("R", "C", weight=2)
G.add_edge("C", "M", weight=1)
G.add_edge("Z", "Ho", weight=2)
G.add_edge("T", "Ho", weight=5)
G.add_edge("D", "R", weight=7)
G.add_edge("D", "Ho", weight=11)
G.add_edge("T", "Ac", weight=9)
G.add_edge("Z", "F", weight=1)
G.add_edge("Cr", "C", weight=8)
G.add_edge("R", "Sp", weight=12)
G.add_edge("A", "D", weight=5)
G.add_edge("Sc", "T", weight=4)
G.add_edge("W", "Ac", weight=2)
G.add_edge("H", "Do", weight=5)
G.add_edge("An", "A", weight=1)
G.add_edge("S", "D", weight=3)
G.add_edge("Do", "W", weight=4)
G.add_edge("My", "Cr", weight=6)
G.add_edge("B", "Do", weight=3)
G.add_edge("T", "F", weight=3)
G.add_edge("B", "My", weight=2)
G.add_edge("Sp", "W", weight=9)
G.add_edge("An", "M", weight=10)
G.add_edge("C", "S", weight=3)
G.add_edge("Sc", "H", weight=8)
G.add_edge("W", "Ho", weight=4)
G.add_edge("B", "A", weight=2)
G.add_edge("An", "Sc", weight=9)
G.add_edge("Cr", "M", weight=14)
G.add_edge("My", "F", weight=15)
G.add_edge("S", "Z", weight=17)
G.add_edge("T", "An", weight=3)
G.add_edge("H", "Sp", weight=4)
G.add_edge("B", "F", weight=7)
G.add_edge("Do", "D", weight=5)
G.add_edge("W", "Z", weight=18)
G.add_edge("C", "Ac", weight=19)

"""
# draw the graph and show it MUST BE THE LAST TWO LINES
pos = nx.spring_layout(G)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=300)

# edges
nx.draw_networkx_edges(G, pos, width=1)

# node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight="bold", font_color="white")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

plt.axis("off")
plt.savefig("prims.png")
"""

# Solution Code for MST Image
G = nx.minimum_spanning_tree(G, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
# plt.savefig("primsoutput.png")

# Edges for MST
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(sorted(sorted(e) for e in edgelist))

