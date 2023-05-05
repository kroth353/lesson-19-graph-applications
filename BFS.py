import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()

# size of figure
plt.figure(figsize=(9,9))

# data for graph
graph.add_edge('JB', 'RR')
graph.add_edge('JB', 'OW')
graph.add_edge('JB', 'VV')
graph.add_edge('JB', 'JS')
graph.add_edge('JB', 'NP')
graph.add_edge('AS', 'VV')
graph.add_edge('AS', 'RW')
graph.add_edge('SJ', 'MR')
graph.add_edge('SJ', 'JR')
graph.add_edge('SJ', 'NP')
graph.add_edge('SJ', 'AH')
graph.add_edge('SJ', 'RW')
graph.add_edge('SJ', 'Z')
graph.add_edge('RR', 'OW')
graph.add_edge('RR', 'IF')
graph.add_edge('RR', 'DF')
graph.add_edge('MR', 'IF')
graph.add_edge('MR', 'JL')
graph.add_edge('MR', 'LD')
graph.add_edge('MR', 'AH')
graph.add_edge('OW', 'VV')
graph.add_edge('OW', 'IF')
graph.add_edge('OW', 'JS')
graph.add_edge('OW', 'NP')
graph.add_edge('OW', 'RW')
graph.add_edge('VV', 'IF')
graph.add_edge('VV', 'NP')
graph.add_edge('VV', 'DF')
graph.add_edge('VV', 'RW')
graph.add_edge('IF', 'JR')
graph.add_edge('IF', 'LD')
graph.add_edge('IF', 'DF')
graph.add_edge('JS', 'ER')
graph.add_edge('JS', 'AH')
graph.add_edge('JS', 'JH')
graph.add_edge('ER', 'DF')
graph.add_edge('ER', 'AH')
graph.add_edge('JL', 'JR')
graph.add_edge('JL', 'LD')
graph.add_edge('JL', 'JH')
graph.add_edge('JL', 'SC')
graph.add_edge('JR', 'NP')
graph.add_edge('DF', 'JH')
graph.add_edge('JH', 'SC')




position = nx.spring_layout(graph)

# nodes
nx.draw_networkx_nodes(graph, position, node_size=400)

# edges
nx.draw_networkx_edges(graph, position, width=1)

# node labels
nx.draw_networkx_labels(graph, position, font_size=10, font_family="sans-serif", font_weight="bold", font_color="white")

plt.show()



# Graph
start_node = 'AS'
end_node = 'JL'
path = []

bfs_tree = nx.bfs_tree(graph, start_node)
path_nodes = nx.shortest_path(bfs_tree, source=start_node, target=end_node)

path = []
for i in range(0, len(path_nodes) - 1):
    path.append(path_nodes[i])
    path.append(path_nodes[i+1])

# create a subgraph with shortest path from Adam Sandler and JH
sub = graph.subgraph(path)

# Draw the subgraph using matplotlib
position = nx.spring_layout(graph)
nx.draw(sub, position, with_labels=True)
plt.show()

finalPath = sorted(set(path), key=path.index)
print(finalPath)
print("Smallest Degree: " + str((len(finalPath) - 1)))
