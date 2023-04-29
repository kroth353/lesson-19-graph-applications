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
It is the release day for a movie you have been looking forward to for months. You need to get to the movie theater (on 17th street) from your house(on 2nd street). You usually take a longer route because it is prettier but you're running late for the movie and need to figure out the shortest path to get to the theater. 
> **Formal Description**:
>  * Input: A series of edges representing the different travel paths, whose weights represent the time it takes to travel along that particular path. The nodes represent the streets taken on that particular path.
>  * Output: The shortest path between second street and seventeenth street 

**Graph Problem/Algorithm**: SSSP


**Setup code**:
```python
Roads = ["1st 2nd {'weight': 6}", "1st 5th {'weight': 8}", "1st 13th {'weight': 3}", "1st 8th {'weight': 13}", "1st 4th {'weight': 7}",
         "2nd 9th {'weight': 1}", "2nd 6th {'weight': 17}", "2nd 15th {'weight': 8}",
         "3rd 18th {'weight': 18}", "3rd 12th {'weight': 3}", "3rd 20th {'weight': 23}", "3rd 5th {'weight': 4}",
         "4th 3rd {'weight': 2}", "4th 16th {'weight': 8}", "4th 19th {'weight': 4}", "4th 10th {'weight': 14}",
         "5th 13th {'weight': 17}", "5th 17th {'weight': 20}", "5th 15th {'weight': 10}", "5th 18th {'weight': 6}",
         "6th 11th {'weight': 3}", "6th 19th {'weight': 5}", "6th 12th {'weight': 2}", "6th 7th {'weight': 8}",
         "7th 14th {'weight': 2}", "7th 8th {'weight': 9}", "7th 20th {'weight': 4}",
         "8th 12th {'weight': 8}", "8th 17th {'weight': 2}",
         "9th 14th {'weight': 4}", "9th 6th {'weight': 11}", "9th 16th {'weight': 10}",
         "10th 20th {'weight': 15}", "10th 11th {'weight': 3}"]

```
**Visualization**:


![Dijkstra's Algorithm Graph](dijkstra.png)
**Solution code:**
```python
import networkx as nx

G = nx.parse_edgelist(Roads, nodetype=str)
print(nx.dijkstra_path(G, "2nd", "17th", weight = 'weight'))
```

**Output**
```python
['2nd', '9th', '14th', '7th', '8th', '17th']
```
**Interpretation of Results**: The shortest path is to travel from your house on second street and turn onto 9th street. From there you will turn onto 14th street, next onto 7th street, then onto 8th street, and finally you will turn onto 17th street to reach the movie theater.

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
# Graph
G= nx.minimum_spanning_tree(G, weight='weight', algorithm='prim', ignore_nan=False)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.show()

# Edges 
mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(sorted(sorted(e) for e in edgelist))
```

**Output**
![Prim's Algorithm Output](primsoutput.png)
```
[['A', 'An'], ['A', 'B'], ['A', 'D'], ['Ac', 'W'], ['An', 'T'], ['B', 'Do'], ['B', 'My'], ['C', 'M'], ['C', 'R'], ['C', 'S'], ['Cr', 'My'], ['D', 'S'], ['Do', 'H'], ['Do', 'W'], ['F', 'T'], ['F', 'Z'], ['H', 'Sp'], ['Ho', 'Z'], ['Sc', 'T']]
```

**Interpretation of Results**: Depending on what genres your friend likes, you can figure out which genres to recommend to them and which genres to not recommend. 

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