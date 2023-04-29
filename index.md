# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Kayla Roth : kjroth@udel.edu
* Mercedes Mathews : mmathews@udel.edu
* Sam Glover : sjglover@udel.edu
* Yazmeen Elzamek : yelzamek@udel.edu


Description of project

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

**Visualization**:

![Dijkstra's Algorithm Graph](dijkstra.png)

**Solution code:**
import networkx as nx

G = nx.parse_edgelist(Roads, nodetype=str)
print(nx.dijkstra_path(G, "2nd", "17th", weight = 'weight'))


**Output**

['2nd', '9th', '14th', '7th', '8th', '17th']

**Interpretation of Results**:

# Second Problem Title

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