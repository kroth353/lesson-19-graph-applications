import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # create a new Graph

# direct requirements get a single directed edge
G.add_edge("Romance", "Comedy", weight=2)
G.add_edge("Romance", "Zombie", weight=50)
G.add_edge("Comedy", "Musical", weight=1)
G.add_edge("Zombie", "Horror", weight=2)
G.add_edge("Thriller", "Horror", weight=5)
G.add_edge("Drama", "Romance", weight=7)
G.add_edge("Drama", "Horror", weight=11)
G.add_edge("Thriller", "Action", weight=9)
G.add_edge("Zombie", "Fantasy", weight=1)
G.add_edge("Crime", "Comedy", weight=8)
G.add_edge("Romance", "Sports", weight=12)
G.add_edge("Animation", "Drama", weight=5)
G.add_edge("Sci Fi", "Thriller", weight=4)
G.add_edge("Western", "Action", weight=2)
G.add_edge("Historical", "Documentary", weight=5)
G.add_edge("Anime", "Animation", weight=1)
G.add_edge("Satire", "Drama", weight=3)
G.add_edge("Documentary", "Western", weight=4)
G.add_edge("Mystery", "Crime", weight=6)
G.add_edge("Biographical", "Documentary", weight=3)
G.add_edge("Thriller", "Fantasy", weight=3)

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
