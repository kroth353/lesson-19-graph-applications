import json
import networkx as nx
import os
import sys
print(os.path.dirname(sys.executable))

dictionary = open('graph.json')
graph = json.load(dictionary)
networkxGraph = nx.cytoscape_graph(dictionary, name = "Marvel Box Office", ident = "dijkstra")
solution = nx.dijkstra_path(networkxGraph, 261, 2800, "")

print(solution)