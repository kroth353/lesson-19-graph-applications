import networkx as nx
import graph.json as graph
import os
import sys
print(os.path.dirname(sys.executable))

dictionary = graph.load(open('graph.json'))
networkxGraph = cytoscape_graph(dictionary, name = "Marvel Box Office", ident = "dijkstra")
solution = dijkstra_path(networkxGraph, 261, 2800, "")

print(solution)