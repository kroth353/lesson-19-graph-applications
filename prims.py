import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # create a new Graph

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

# draw the graph and show it MUST BE THE LAST TWO LINES
pos = nx.spring_layout(G)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=50)

# edges
nx.draw_networkx_edges(G, pos, width=1)

# node labels
nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif", font_weight="bold")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

plt.axis("off")
plt.show()
