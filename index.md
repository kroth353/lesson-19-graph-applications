# Graphing with Movies

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Kayla Roth : kjroth@udel.edu
* Mercedes Mathews : mmathews@udel.edu
* Sam Glover : sjglover@udel.edu
* Yazmeen Elzamek : yelzamek@udel.edu


In our site, we created 4 different graphs that all revolve around the central concept of Movies. We focused on Dijkstra's Algorithm, Prim's Algorithm, Breadth-first Search, and Depth-first Search.

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# Dijkstras Algorithm

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: SSSP


**Setup code**:

```python
```

**Visualization**:

![Dijkstra's Algorithm Graph](graphviz.png)

**Solution code:**

```python

import graph.json as graph
dictionary = graph.load(open('graph.json'))
networkxGraph = cytoscape_graph(dictionary, name = "Marvel Box Office", ident = "dijkstra")
solution = dijkstra_path(networkxGraph, 261, 2800, "")
```

**Output**
```
print(solution)
```

**Interpretation of Results**:

# Prim's Algorithm

**Informal Description**: You want to recommend some movies to a friend. You know what genre of movies your friend likes. By using your friend's preferences, you want to find the smallest set of movie genres that are connected to each other and that will fit your friend's preferences. 
Each movie genre is given an abbreviation. The abbreviations are as follows:
- A = Animation
- Ac = Action 
- An = Anime 
- B = Biographical 
- C = Comedy 
- Cr = Crime 
- D = Drama 
- Do = Documentary 
- F = Fantasy 
- H = Historical 
- Ho - Horror 
- M = Musical 
- My = Mystery 
- R = Romance 
- S = Satire
- Sc = Sci Fi  
- Sp = Sports
- T = Thriller 
- W = Western 
- Z = Zombie 

> **Formal Description**:
>  * Input: An undirected graph, consisting of movie genres as nodes and the edges represent the similarity between the genres
>  * Output: A Minimum Spanning Tree 

**Graph Problem/Algorithm**: MST


**Setup code**:

```python
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
plt.show()
```

**Visualization**:

![Prim's Algorithm Graph](prims.png)

**Solution code:**

```python
G = nx.minimum_spanning_tree(G, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()
```

**Output**
![Prim's Algorithm Output](primsoutput.png)
```
```

**Interpretation of Results**:

# Third Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: SSSP


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

# Fourth Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: SSSP


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**: