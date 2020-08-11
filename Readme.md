# GRAPH-SIMPLE

# Introduction

This program explores different simple graphs built either by table or by function.
Determine the connected components and calculate the shortest path between two random vertices.

Only undirected simple graphs are supported.

The computation of the shortest path is very powerful for the random graph g_06
example: for a graph of 5 million vertices and 15 million random edges, the calculation takes less than three minutes.

It is possible to fix the random number generator to always have the same graph with the function
seed (n) where n is an integer.


# Usage
python3.8 graph-simple.py

The command chmod +x graph-simple.py, the program can be ran directly in terminal


# Tests
python3 -m unittest discover  -p "*test.py" -s ./tests -v


# Results 
Graph name:       G_06 - Random graph\
This graph is undirected, not connected\
have 500_000 vertices, 999_996 edge(s) and 9_588 component(s)  

Bunches | Vertices by bunch
--- | ---
9_215      |    1
344        |    2
27         |    3
1          |    4
1          |    490_012


Shortest path from 330982 to 217306 in graph G_06 is length : 10\
path=[330982, 53551, 173147, 164415, 352668, 461480, 313891, 38808, 406201, 120078, 217306]


# Files
Files | Desc
--- | ---
graphe-simple.py | main program
./util/graph_lib.py | Library of function
./data/some_of_them.py | Some graph describe by table or by function
./test/graphe_test.py | Used by Unittest
Readme.FR.md | This file in French            
Readme.md | This file

## Requirements
1. Python >=3.8
1. (optional) The external CProfileV: pip install CProfileV, see links



# Profiling and trace
python3 -m trace --count -C ./cover/ graphe-simple.py  
Will produce un trace of number of function call for all used function

python3 -m trace --trace -C ./cover/ --timing Graphes.py  
Will produce the file timing.txt with timing trace of all used function.   

python3 -m trace --Count -C ./cover/ --timing Graphes.py  
Will produce a timeline of function call, the result is on ./cover/ folder 

(optional)  
python3 -m cProfile -o output.prf ./graphe-simple.py  
follow by cprofilev -f output.prf   
will produce an output available at http://127.0.0.1:4000




# Useful links

[Glossary of graph theory terms(wikipedia)](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms)

[Some definitions ](https://www.momirandum.com/graphes/theorie-des-graphes/Connexite.html)

[Introduction to  A* algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html#breadth-first-search)  

[Profiling with cprofilev](https://github.com/ymichael/cprofilev)  
  


#  TODO / DONE
- [ ] Adjacency matrix
- [ ] Incidence Matrix
- [ ] Dual of a graph 
- [ ] Graph diameter   
- [ ] Function  is_isomorphic(graph1, graph2)
- [ ] Function is_eulerian
- [ ] Function is_Hamiltonian
- [ ] Function is_planar()    
- [ ] Better represantation of Bunches and Vertices by bunch
- [ ] Found all possible path between two edges, exist ? who is the better ?
- [ ] DFS is accurate but not fast at all compared to BFS.
- [ ] The default value 1 of the edge is not used but is could be used for futur development.

Now it's time for improvement and your comments!