import networkx as nx
import matplotlib.pyplot as plt
"""
G = nx.Graph()

G.add_edge("Art Institute of Chicago", "Alcatraz", weight=3)
G.add_edge("Art Institute of Chicago", "Bates Motel", weight=2)
G.add_edge("Bates Motel", "Buckingham Palace", weight=2, length=10)
G.add_edge("Alcatraz", "Central Market", weight=2, length=10)
G.add_edge("Buckingham Palace", "Grand Central Station", weight=2)
G.add_edge("Buckingham Palace", "Karaoke Kan", weight=2)
G.add_edge("King's Cross Station", "Karaoke Kan", weight=2)
G.add_edge("Lincoln Memorial", "Buckingham Palace", weight=2)
G.add_edge("Randy's Donuts", "Alcatraz", weight=2)
G.add_edge("Harbor Freeway", "Llanerch Diner", weight=2)
G.add_edge("Bates Motel", "MOMA", weight=2)
G.add_edge("Swan House", "King's Cross Station", weight=2)
G.add_edge("Tiffany & Co.", "Central Market", weight=2)
G.add_edge("Swan House", "Plaza Hotel", weight=2)
G.add_edge("Getty Center", "Lincoln Memorial", weight=2)
G.add_edge("Karaoke Kan", "Stoke Park", weight=2)
G.add_edge("Point Dunne", "Pike Place Market", weight=2)
G.add_edge("MacArthur Park", "Pike Place Market", weight=2)
G.add_edge("Point Dunne", "Katz's Deli", weight=2)
G.add_edge("Harbor Freeway", "Plaza Hotel", weight=2)

pos = nx.spring_layout(G, seed=500)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=50)

# edges
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_edges(
    G, pos, width=6, alpha=0.5, edge_color="b")

# node labels
nx.draw_networkx_labels(G, pos, font_size=6, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
plt.axis("off")
plt.show()
"""

G = nx.Graph() # create a new Graph

# direct requirements get a single directed edge
G.add_edge("Art Institute of Chicago", "Alcatraz", weight=3)
G.add_edge("Art Institute of Chicago", "Bates Motel", weight=2)
G.add_edge("Bates Motel", "Buckingham Palace", weight=2)
G.add_edge("Alcatraz", "Central Market", weight=2)
G.add_edge("Buckingham Palace", "Grand Central Station", weight=2)
G.add_edge("Buckingham Palace", "Karaoke Kan", weight=2)
G.add_edge("King's Cross Station", "Karaoke Kan", weight=2)
G.add_edge("Lincoln Memorial", "Buckingham Palace", weight=2)
G.add_edge("Randy's Donuts", "Alcatraz", weight=2)
G.add_edge("Harbor Freeway", "Llanerch Diner", weight=2)
G.add_edge("Bates Motel", "MOMA", weight=2)
G.add_edge("Swan House", "King's Cross Station", weight=2)
G.add_edge("Tiffany & Co.", "Central Market", weight=5)
G.add_edge("Swan House", "Plaza Hotel", weight=2)
G.add_edge("Getty Center", "Lincoln Memorial", weight=2)
G.add_edge("Karaoke Kan", "Stoke Park", weight=2)
G.add_edge("Point Dunne", "Pike Place Market", weight=2)
G.add_edge("Alcatraz", "Pike Place Market", weight=2)
G.add_edge("Point Dunne", "Lincoln Memorial", weight=2)
G.add_edge("Harbor Freeway", "Plaza Hotel", weight=2)
G.add_edge("Harbor Freeway", "Stoke Park", weight=2)
G.add_edge("Point Dunne", "MOMA", weight=2)
G.add_edge("King's Cross Station", "Randy's Donuts", weight=2)
G.add_edge("Plaza Hotel", "Llanerch Diner", weight=2)
G.add_edge("Getty Center", "Plaza Hotel", weight=2)
G.add_edge("Harbor Freeway", "Art Institute of Chicago", weight=2)
G.add_edge("Getty Center", "Plaza Hotel", weight=2)
G.add_edge("Llanerch Diner", "Tiffany & Co.", weight=2)
G.add_edge("King's Cross Station", "Lincoln Memorial", weight=2)
G.add_edge("MOMA", "Tiffany & Co.", weight=2)
G.add_edge("Grand Central Station", "Swan House", weight=2)


# FOR A WEIGHTED GRAPH
# G.add_weighted_edges_from([('CISC 108', 'CISC 181', 1)]) # add nodes & edges

# draw the graph and show it MUST BE THE LAST TWO LINES
pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, with_labels=True, font_weight="bold", font_size=6)
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=6)
plt.axis("off")
plt.show()