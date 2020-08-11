""" Library  of functions """
"""
    graphe_lib.py  
    Created by lwi19
    Copyright © 2020 Louis Plouffe. All rights reserved.
"""


import itertools as it
from collections import deque
from dataclasses import dataclass
from pprint import PrettyPrinter
from random import sample, random, seed

# Uncomment this line below to generate always the same random graph (Erdos and Random),
# seed(2146)


@dataclass
class Graph:
    """
    Simple graph defined with the adjacency list.
    :graph_dict - a graph defined with this dictionary format
    see some_of_them.py to see how to write them
    {
        vertex: {neighbour: value, neighbour: value...},
        vertex: {neighbour: value, neighbour: value...},...
    }
    :name: name of the graph
    """
    # TODO: The default value 1 of the edge is not used but is could be used for futur development.
    # dictionary of graph, name and directed
    graph_dict: dict
    name: str
    directed = None
    # dictionary of vertices and visited vertices.
    visited: dict = ()
    vertices = set()

    def __post_init__(self):
        """
        The post_init is used to ensure that visited and vertices variables are initialised
        :return:
        """
        self.init_vertices()
        self.init_visited()

    def init_vertices(self):
        """
        :return: initialisation of set of all vertices.
        """
        self.vertices = set(self.graph_dict)

    def init_visited(self):
        """
        Initialisation of dictionary of visited vertex.
        """
        self.visited = dict.fromkeys(self.graph_dict.keys(), False)

    def is_graph(self):
        """
        Determine if the adjacency list is a simple graph by testing if
        all values appears as least once time in the key list.
        :return True if it is a correct graph
        """
        result = True
        for s in self.graph_dict.values():
            for t in s:
                if t not in self.graph_dict.keys():
                    result = False
                    break
        return result

    def edges(self):
        """
        Set for all edges in tuples format
        :return set for all edges in tuples format.
        Utilisation of set instead of list is for a better performance.
        """

        # Utilisation of set is more efficient than list with this function
        set_of_edges = set()

        if self.is_directed():
            [set_of_edges.add((vertex, neighbour)) for vertex in self.graph_dict
                for neighbour in self.graph_dict.get(vertex)]
        else:
            [set_of_edges.add((vertex, neighbour)) for vertex in self.graph_dict
                for neighbour in self.graph_dict.get(vertex)
                if (neighbour, vertex) not in set_of_edges]

        # return sorted(list(set_of_edges))
        # return list(set_of_edges)
        return set_of_edges

    def edges_for_directed(self):
        """
        Complete list of edges for an directed graph only.
        Used by directed() function.
        if the graph is undirected, the edges are counted twice.
        :return: set of all edges in tuple format

        """
        set_of_edges_for_directed = []
        [set_of_edges_for_directed.append((vertex, neighbour)) for vertex in self.graph_dict
            for neighbour in self.graph_dict.get(vertex)]
        return set_of_edges_for_directed

    def is_edge(self, vertex_one, vertex_two):
        """
        Find if it is a valid edge or not,
        :param:  vertex_one, vertex_two
        :return: True if vertices are present and connected by an edge
        """
        result = vertex_two in self.neighbours(vertex_one)
        return bool(result)

    def is_directed(self):
        """
        Find the direction of the graph. Every edges have to be visited.
        :return  False: undirected, True: directed
        """
        # The edge list is used as a set of tuples to be more efficient.
        # If self.directed is already found True or False, it's not necessary to re-browse all edges.

        if self.directed is None:
            all_edges = set(self.edges_for_directed())
            result = bool(list(it.filterfalse(lambda x: tuple(reversed(x)) in all_edges, all_edges)))
            self.directed = result
        else:
            result = self.directed
        return result

    def one_random_vertex(self):
        """
        One vertex randomly chosen
        :return one vertex
        """
        return sample(self.vertices, 1)[0]

    def two_random_vertices(self):
        """
        Find two random distinct vertices of the graph.
        :return: two vertices or False if it's not possible to extract.
        """
        # TODO: ensure that they are connected. (could be long to calculate each time)
        if rep := sample(self.vertices, 2):
            vertex_one, vertex_two = rep
            return vertex_one, vertex_two
        else:
            return False

    def add_vertex(self, vertex):
        """
        Add one vertex, even if it is already here.
        :param vertex:
        """
        # TODO: should return boolean value for the success.

        if vertex not in self.vertices:
            self.graph_dict[vertex] = {}        # add the vertex in adjacency list

    def add_edge(self, vertex_one, vertex_two, directed=False):
        """
        Add an edge if and only if the two vertices must exist and are not connected.
        :param vertex_one:
        :param vertex_two:
        :param directed: False by default for undirected graph
        :return: True if ok, False if it is not possible to add edge.
        """
        # If the graph is directed : only one entry is add in the adjacency list

        if vertex_one in self.vertices and vertex_two in self.vertices:
            if vertex_two not in self.neighbours(vertex_one):
                self.graph_dict[vertex_one].update({vertex_two: 1})
                if not directed:
                    self.graph_dict[vertex_two].update({vertex_one: 1})
            return True
        else:
            return False

    def delete_edge(self, vertex_one, vertex_two, directed=False):
        """
        Remove one edge only.
        :param vertex_one:
        :param vertex_two:
        :param directed: False by default for undirected graph
        :return: True if deletion success, False it is not possible
        """

        # if the graph is undirected (default) the 'dual' edge is removed. (v1,v2) and (v2, v1).

        if self.is_edge(vertex_one, vertex_two):
            vertex_one_neighbours = self.neighbours(vertex_one)
            vertex_one_neighbours.pop(vertex_two)
            if not directed and vertex_one != vertex_two:   # Stop, no loop permitted
                vertex_two_neighbours = self.neighbours(vertex_two)
                vertex_two_neighbours.pop(vertex_one)
            return True
        else:
            return False

    def delete_vertex(self, vertex):
        """
        Remove one vertex and all edges connected to this vertex
        :param vertex:
        """
        # TODO: should return boolean value for the success.

        if self.neighbours(vertex) is not None:
            neighbourhood = list(self.neighbours(vertex))
            for elem in neighbourhood:
                self.delete_edge(elem, vertex)
            self.graph_dict.pop(vertex)

    def degree(self, vertex):
        """
        Find the number of adjacent edge of one vertex.
        :param  vertex:  from where is counted.
        :return: degree
        """
        return len(self.graph_dict.get(vertex))

    def degrees(self):
        """
        List of degree of all vertices.
        :return: dictionary of {vertex: degree,...}
        """

        list_of_degree = {}
        for elem in self.vertices:
            list_of_degree.update({elem: self.degree(elem)})
        return list_of_degree

    def neighbours(self, vertex):
        """
        Direct neighbours of vertex, they are in the same row in the adjacency list.
        :param: vertex: one given vertex
        :return: list of directs neighbours of vertex.
        """
        return self.graph_dict.get(vertex)

    def extract_components(self, style="BFS"):
        """
        Exploration of the graph by decomposition of connected components.

        :param style: style is Breadth or Deep First Search ("BFS" or "DFS"). BFS is the default.
        :return tuple with two dictionary:
            dictionary of vertices grouped by component
            summary of this dictionary

        A simple graph is separated in different components
        To find a component, the function start from one vertex then 'visit' each of his neighbours and their neighbours(or visited).
        When no more neighbours are reachable, all visited vertices are considered as a component.

        To find others components, the method is applied to remaining of the not visited vertices.
        This make a dictionary where the key is a simple index(1,2,3...) and the values are the vertices on the same component.
        """

        def group_components(gr):
            """
            Summarize the result from extract.
            :param gr: dictionary of vertices grouped by component
            :return: dictionary of all components
                {key    : number of vertices by component
                 values : number of components with the same number of vertices}
                ex: bunch = {1: 71, 2: 7, 3: 4, 403: 1}
            """
            g_comp = {}
            for elem in gr:
                v = len(gr.get(elem))
                if g_comp.get(v):
                    g_comp[v] += 1
                else:
                    g_comp[v] = 1

            g_comp = dict(sorted(zip(g_comp.keys(), g_comp.values())))
            return g_comp
        self.init_visited()
        components = {}
        comp_conx = 0
        for s in self.vertices:
            if not self.visited.get(s):
                comp_conx += 1
                if style == "BFS":
                    components[comp_conx] = self.breadth_first_search(s)
                else:
                    components[comp_conx] = self.depth_first_search(s)
        return components, group_components(components)

    def depth_first_search(self, vertex):
        """
        Exploration from a vertex by the Deep First Search algorithm (DFS)
        : param vertex : a vertex to start the exploration
        :return: all connected vertices to the vertex (ie one component)
        """
        # FIXME: not optimized for performance (not at all!)

        stack, dfs_result = [vertex], []
        self.visited[vertex] = True
        while stack:
            vertex = stack.pop()
            if vertex in dfs_result:
                continue
            dfs_result.append(vertex)
            for neighbor in self.neighbours(vertex):
                stack.append(neighbor)
                self.visited[neighbor] = True

        return dfs_result

    def breadth_first_search(self, vertex):
        """
        Exploration from a vertex by the Breadth First Search algorithm (BFS)
        : param vertex : a vertex to start the exploration.
        :return: all connected vertices to the vertex (ie one component).
        """
        # Module deque is very helpful if you have to popleft

        stack = deque()
        stack.append(vertex)
        accu = deque()
        accu.append(vertex)
        self.visited[vertex] = True
        while stack:
            v = stack.popleft()
            for w in self.neighbours(v):
                if not self.visited.get(w):
                    stack.append(w)
                    self.visited[w] = True
                    accu.append(w)
        return list(accu)

    def find_shortest_path(self, vertex_one, vertex_two):
        """
        BFS variante of shortest path algorithm with deque instead of list or SimpleQueue.
        it's particularly fast.
        : vertex_one, vertex_two : start and stop vertex.
        :return: list of the shortest path from vertex_one to vertex_two. False if not path found
        """
        # more here: https://www.redblobgames.com/pathfinding/a-star/introduction.html#breadth-first-search

        if vertex_one in self.vertices and vertex_two in self.vertices:
            stack = deque()
            stack.append(vertex_one)
            accu = {vertex_one: None}
            v = vertex_two
            path = deque()
            while stack:
                v = stack.pop()
                if v == vertex_two:
                    break

                for w in self.neighbours(v):
                    if w not in accu:
                        stack.appendleft(w)
                        accu[w] = v

            if vertex_two not in accu:
                return False
                # here, the path is found. we can reconstruct the path from accu dictionary
            while v != vertex_one:
                path.appendleft(v)
                v = accu.get(v)
            path.appendleft(vertex_one)
        else:
            return False
        return list(path)

# end of Graph class


def is_p_greater_than_random(p):
    """
    :return: True iff p is greater than a random number between 0 and 1
    """
    return bool(p > random())


def list_to_dict(graph_list):
    """
    Convert a graph in list mode to a dictionary and by put value 1 at each edge
    Only used to convert external graphs.
    Example: {0:(1,2), 1:(0,2)}  -->  {0: {1: 1, 2: 1}, 1: {0: 1, 2: 1}}
    :param graph_list:

    """
    graph_dict = {}
    for i in graph_list:
        elem = {key: 1 for key in graph_list[i]}
        graph_dict.update({i: elem})

    return graph_dict


def vertices_generation(number_of_vertices):
    """
    Generate the vertices list
    :param number_of_vertices:
    :return: vertices list in format [0, 1, 2, 3...]

    """
    # here, the list is much more efficient than set

    return [s for s in range(1, number_of_vertices + 1)]


def random_graph(number_of_vertices, number_of_nodes, name="Random graph", directed=False):
    """
    Construction of graph when the number of vertices and edges is fixed.
    The edges are generated by a series of two random vertices.
    Notice: this is a simple graph and loop are not permitted.
    :param number_of_vertices:
    :param number_of_nodes:  should be smaller than the maximum n*(n-1)/2
    :param name:
    :param directed: False by default for undirected graph
    :return: random graph
    """

    list_of_vertices = vertices_generation(number_of_vertices)
    constructed_graph = Graph({s: {} for s in list_of_vertices}, name)

    for _ in range(number_of_nodes):
        vertex_one, vertex_two = sample(list_of_vertices, 2)
        constructed_graph.add_edge(vertex_one, vertex_two, directed)

    return constructed_graph


def erdos_graph(number_of_vertices, prob=0.10, name="Erdos_graph", directed=False):
    """
    Construction of simple, non-directed and random graph.
    The number of vertices are fixed and the number of edges are given by the probabilities.

    prob = 0.0 -> graph with all vertices and no edges.
    prob = 1.0 -> complete graph with maximum number of edges.
    :param number_of_vertices:
    :param prob: the probability of presence of the edge, must be >=0 and <=1, 1 mean a complete graph. Default = 0.1
    :param name: name of the graph. Default "Erdos_graph"
    :param directed: False by default for undirected graph
    :return : the Erdos graph.
    """
    # The comprehension list is used to give every possible case of edge.
    # The edge is created only when the condition based on probability is meet
    list_of_vertices = vertices_generation(number_of_vertices)
    constructed_graph = Graph({s: {} for s in list_of_vertices}, name)
    [constructed_graph.add_edge(s, t, directed)
     for s in range(1, number_of_vertices + 1)
     for t in range(s, number_of_vertices + 1)
     if is_p_greater_than_random(prob) and s != t]
    return constructed_graph


def complete_graph(number_of_vertices, name="Complet graph", directed=False):
    """
    Construction of a complete graph.
    The number of edges is exactly  n*(n-1)/2 (where n is the number of vertices)
    :param number_of_vertices:
    :param name:
    :param directed:  False for undirected graph
    :return: the complete graph

    """
    # The comprehension list is used to give every possible case of edge.
    list_of_vertices = vertices_generation(number_of_vertices)
    constructed_graph = Graph({s: {} for s in list_of_vertices}, name)
    [constructed_graph.add_edge(s, t, directed)
        for s in range(1, number_of_vertices + 1)
        for t in range(s, number_of_vertices + 1)
        if s != t]

    return constructed_graph


def print_adjacency_list(self):
    """
    print the adjacency list of the graph
    """
    pretty_print = PrettyPrinter(indent=4)
    print("Adjacency list: ", end="\n")
    pretty_print.pprint(self.graph_dict)


def print_graph(self):
    """
    Print all vertices and edges in simple form.
    """

    set_of_vertices = self.vertices
    all_edges = self.edges()
    print("Set of vertices:  {}".format(set_of_vertices))
    print("set of edges: {}".format(all_edges))
    print("Number of edges : {}".format(len(all_edges)))
    print("Number of nodes : {}".format(len(set_of_vertices)))


def print_components(bunch):
    """
    """
    heading = "Bunches \tVertices by bunch"
    # print each different group of component line by line.

    print(heading)
    for k, v in bunch.items():
        print(f"{v:0_}\t\t{k:0_}")
    print("\n")


def presentation(self):
    """
    Explore and print properties of the simple graph.
    like orientation , number of vertices and edges, number of components...
    """

    # Two styles of exploration is used. "BFS" seems to be much efficient

    group_components, summary_components = self.extract_components(style="BFS")
    directed_desc = "directed" if self.is_directed() else "undirected"
    connexe_desc = "connected" if len(group_components) == 1 else "not connected"
    number_of_vertices = len(self.vertices)
    number_of_edges = len(self.edges())

    message = (
        f"Graph name:       {self.name} \n"
        f"This graph is {directed_desc}, {connexe_desc}\n"
        f"have {number_of_vertices:0_} vertices, "
        f"{number_of_edges:0_} edge(s) and "
        f"{len(group_components):0_} component(s)"
    )
    print(message)
    print_components(summary_components)
    # Uncomment these lines below to print all the graph or the adjacency list.
    # print_graph(self)
    # print_adjacency_list(self)
