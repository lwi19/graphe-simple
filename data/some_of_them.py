"""
    some_of_them.py
    Created by lwi19
    Copyright © 2020 Louis Plouffe. All rights reserved.
"""

"""
 Some typical graphs definition.
 Two format is possible:  Adjacency list or by function:

    graph_name =
           {
           vertex: {neighbour: value, neighbour: value...},
           vertex: {neighbour: value, neighbour: value...},...
           }
    g_XX = Graph(graph_name, "G_01")
    g_XX is the variable name used in all programs.

 Special graphs are calculated instead of explicitly listed. Like "random_graph", "erdos_graph", "complete_graph"
 In these case, the call of "init_graph" is done directly on their definition and they have to be imported in this module.

"""

from util.graph_lib import Graph, random_graph, erdos_graph, complete_graph

"""
    List of samples graphs

    Graphs explicitly constructed
    g_01: Undirected and disconnected graph
    g_02: Undirected and disconnected graph
    g_03: Undirected and connected graph
    g_04: Undirected and disconnected graph
    g_05: Undirected and disconnected graph

    Random graphs
    g_06: Undirected random graph - the number of edge is randomly choose  (formally Erdős uniform model)
    g_07: Undirected random graph - each vertices have a probability to appear (Erdős binomial model) 

    Complete graph
    g_08: Undirected complete graph with the maximum number of edges
"""

# Undirected and disconnected graph
#
graph_g01 = {
    0: {3: 1},
    1: {2: 1},
    2: {1: 1, 3: 1, 4: 1},
    3: {0: 1, 2: 1},
    4: {2: 1},
    5: {},
}
g_01 = Graph(graph_g01, "G_01")

graph_g02 = {
    1: {31: 1, 44: 1, 66: 1},
    2: {74: 1},
    3: {86: 1},
    4: {90: 1},
    5: {65: 1},
    6: {11: 1, 34: 1, 96: 1},
    7: {67: 1},
    8: {52: 1, 59: 1},
    9: {49: 1},
    10: {},
    11: {6: 1},
    12: {15: 1, 79: 1, 97: 1},
    13: {45: 1, 95: 1, 98: 1},
    14: {},
    15: {12: 1, 41: 1, 46: 1, 64: 1, 88: 1},
    16: {85: 1},
    17: {31: 1, 32: 1, 82: 1, 84: 1},
    18: {19: 1},
    19: {18: 1},
    20: {52: 1, 85: 1},
    21: {65: 1},
    22: {25: 1, 77: 1, 93: 1},
    23: {35: 1, 39: 1},
    24: {32: 1},
    25: {22: 1, 44: 1},
    26: {},
    27: {34: 1, 46: 1, 62: 1},
    28: {37: 1, 51: 1},
    29: {},
    30: {78: 1},
    31: {1: 1, 17: 1, 36: 1, 52: 1, 55: 1, 65: 1},
    32: {17: 1, 24: 1, 36: 1, 64: 1, 80: 1},
    33: {},
    34: {6: 1, 27: 1, 74: 1},
    35: {23: 1, 37: 1},
    36: {31: 1, 32: 1, 48: 1},
    37: {28: 1, 35: 1, 41: 1, 71: 1},
    38: {39: 1, 79: 1},
    39: {23: 1, 38: 1, 57: 1, 65: 1, 77: 1},
    40: {},
    41: {15: 1, 37: 1, 98: 1},
    42: {},
    43: {69: 1},
    44: {1: 1, 25: 1, 89: 1},
    45: {13: 1, 76: 1, 93: 1},
    46: {15: 1, 27: 1, 92: 1},
    47: {},
    48: {36: 1},
    49: {9: 1, 60: 1, 98: 1},
    50: {},
    51: {28: 1, 77: 1, 79: 1, 95: 1},
    52: {8: 1, 20: 1, 31: 1, 75: 1, 89: 1},
    53: {90: 1, 91: 1},
    54: {},
    55: {31: 1, 91: 1, 97: 1},
    56: {77: 1},
    57: {39: 1},
    58: {},
    59: {8: 1, 89: 1},
    60: {49: 1, 66: 1, 69: 1, 78: 1, 87: 1},
    61: {},
    62: {27: 1, 69: 1, 72: 1},
    63: {94: 1},
    64: {15: 1, 32: 1, 66: 1},
    65: {5: 1, 21: 1, 31: 1, 39: 1, 85: 1},
    66: {1: 1, 60: 1, 64: 1, 75: 1},
    67: {7: 1},
    68: {89: 1},
    69: {43: 1, 60: 1, 62: 1, 98: 1},
    70: {},
    71: {37: 1, 81: 1},
    72: {62: 1},
    73: {},
    74: {2: 1, 34: 1, 77: 1},
    75: {52: 1, 66: 1},
    76: {45: 1},
    77: {22: 1, 39: 1, 51: 1, 56: 1, 74: 1},
    78: {30: 1, 60: 1},
    79: {12: 1, 38: 1, 51: 1},
    80: {32: 1},
    81: {71: 1},
    82: {17: 1},
    83: {},
    84: {17: 1},
    85: {16: 1, 20: 1, 65: 1},
    86: {3: 1},
    87: {60: 1},
    88: {15: 1},
    89: {44: 1, 52: 1, 59: 1, 68: 1},
    90: {4: 1, 53: 1},
    91: {53: 1, 55: 1, 97: 1, 100: 1},
    92: {46: 1},
    93: {22: 1, 45: 1},
    94: {63: 1, 97: 1},
    95: {13: 1, 51: 1},
    96: {6: 1},
    97: {12: 1, 55: 1, 91: 1, 94: 1},
    98: {13: 1, 41: 1, 49: 1, 69: 1},
    99: {},
    100: {91: 1}
}
g_02 = Graph(graph_g02, "G_02")

graph_g03 = {
    1: {2: 1},
    2: {1: 1, 3: 1},
    3: {2: 1, 4: 1},
    4: {3: 1, 5: 1},
    5: {4: 1, 6: 1},
    6: {5: 1}
}
g_03 = Graph(graph_g03, "G_03")

graph_g04 = {
    1: {31: 1, 44: 1, 66: 1},
    2: {74: 1},
    3: {86: 1},
    4: {90: 1},
    5: {65: 1},
    6: {11: 1, 34: 1, 96: 1},
    7: {67: 1},
    8: {52: 1, 59: 1},
    9: {49: 1},
    10: {},
    11: {6: 1},
    12: {15: 1, 79: 1, 97: 1},
    13: {45: 1, 95: 1, 98: 1},
    14: {},
    15: {12: 1, 41: 1, 46: 1, 64: 1, 88: 1},
    16: {85: 1},
    17: {31: 1, 32: 1, 82: 1, 84: 1},
    18: {19: 1},
    19: {18: 1},
    20: {52: 1, 85: 1},
    21: {65: 1},
    22: {25: 1, 77: 1, 93: 1},
    23: {35: 1, 39: 1},
    24: {32: 1},
    25: {22: 1, 44: 1},
    26: {},
    27: {34: 1, 46: 1, 62: 1},
    28: {37: 1, 51: 1},
    29: {},
    30: {78: 1},
    31: {1: 1, 17: 1, 36: 1, 52: 1, 55: 1, 65: 1},
    32: {17: 1, 24: 1, 36: 1, 64: 1, 80: 1},
    33: {},
    34: {6: 1, 27: 1, 74: 1},
    35: {23: 1, 37: 1},
    36: {31: 1, 32: 1, 48: 1},
    37: {28: 1, 35: 1, 41: 1, 71: 1},
    38: {39: 1, 79: 1},
    39: {23: 1, 38: 1, 57: 1, 65: 1, 77: 1},
    40: {},
    41: {15: 1, 37: 1, 98: 1},
    42: {},
    43: {69: 1},
    44: {1: 1, 25: 1, 89: 1},
    45: {13: 1, 76: 1, 93: 1},
    46: {15: 1, 27: 1, 92: 1},
    47: {},
    48: {36: 1},
    49: {9: 1, 60: 1, 98: 1},
    50: {},
    51: {28: 1, 77: 1, 79: 1, 95: 1},
    52: {8: 1, 20: 1, 31: 1, 75: 1, 89: 1},
    53: {90: 1, 91: 1},
    54: {},
    55: {31: 1, 91: 1, 97: 1},
    56: {77: 1},
    57: {39: 1},
    58: {},
    59: {8: 1, 89: 1},
    60: {49: 1, 66: 1, 69: 1, 78: 1, 87: 1},
    61: {},
    62: {27: 1, 69: 1, 72: 1},
    63: {94: 1},
    64: {15: 1, 32: 1, 66: 1},
    65: {5: 1, 21: 1, 31: 1, 39: 1, 85: 1},
    66: {1: 1, 60: 1, 64: 1, 75: 1},
    67: {7: 1},
    68: {89: 1},
    69: {43: 1, 60: 1, 62: 1, 98: 1},
    70: {},
    71: {37: 1, 81: 1},
    72: {62: 1},
    73: {},
    74: {2: 1, 34: 1, 77: 1},
    75: {52: 1, 66: 1},
    76: {45: 1},
    77: {22: 1, 39: 1, 51: 1, 56: 1, 74: 1},
    78: {30: 1, 60: 1},
    79: {12: 1, 38: 1, 51: 1},
    80: {32: 1},
    81: {71: 1},
    82: {17: 1},
    83: {},
    84: {17: 1},
    85: {16: 1, 20: 1, 65: 1},
    86: {3: 1},
    87: {60: 1},
    88: {15: 1},
    89: {44: 1, 52: 1, 59: 1, 68: 1},
    90: {4: 1, 53: 1},
    91: {53: 1, 55: 1, 97: 1, 100: 1},
    92: {46: 1},
    93: {22: 1, 45: 1},
    94: {63: 1, 97: 1},
    95: {13: 1, 51: 1},
    96: {6: 1},
    97: {12: 1, 55: 1, 91: 1, 94: 1},
    98: {13: 1, 41: 1, 49: 1, 69: 1},
    99: {},
    100: {91: 1}
}
g_04 = Graph(graph_g04, "G_04")

graph_g05 = {
    1: {25: 1},
    2: {18: 1, 21: 1},
    3: {29: 1, 28: 1},
    4: {28: 1},
    5: {13: 1},
    6: {30: 1, 7: 1},
    7: {9: 1, 30: 1, 6: 1},
    8: {21: 1, 15: 1},
    9: {7: 1},
    10: {19: 1, 16: 1, 21: 1},
    11: {19: 1, 23: 1},
    12: {28: 1, 17: 1, 23: 1, 13: 1, 14: 1, 22: 1},
    13: {16: 1, 21: 1, 5: 1, 12: 1},
    14: {18: 1, 12: 1},
    15: {18: 1, 8: 1},
    16: {13: 1, 10: 1},
    17: {12: 1},
    18: {15: 1, 14: 1, 2: 1, 25: 1, 26: 1},
    19: {10: 1, 21: 1, 11: 1, 24: 1},
    20: {},
    21: {8: 1, 24: 1, 19: 1, 13: 1, 10: 1, 2: 1, 23: 1},
    22: {26: 1, 29: 1, 12: 1},
    23: {25: 1, 11: 1, 12: 1, 21: 1},
    24: {21: 1, 19: 1},
    25: {23: 1, 18: 1, 1: 1},
    26: {22: 1, 18: 1},
    27: {},
    28: {12: 1, 29: 1, 4: 1, 3: 1},
    29: {3: 1, 28: 1, 22: 1},
    30: {6: 1, 7: 1},
}
g_05 = Graph(graph_g05, "G_05")

# Random graph: The number of edges and nodes are fixed but they are randomly spread.
# If the seed is set in graph_lib.py the random will recreate always the same graph.

g_06 = random_graph(500_000, 1_000_000, "G_06 - Random graph")


# Random Erdős graph: The number of edges is fixed but each node are put with a random probability.
# when p = 0: graph with edges but no nodes
# when p = 1: complete graph. All possible nodes are present.
# Erdős and random graph have similar properties.
# If the seed is set in graph_lib.py the random will recreate always the same graph.
g_07 = erdos_graph(2_000, 0.09, "G_07 - Erdős graph")

# Complete graph, all possible edges ( n(n-1)/2 ) are created from the vertices list.
# Warning: number of edges is growing with the order O(n^2) vertices.
g_08 = complete_graph(100, "G_08 - Complete graph")
