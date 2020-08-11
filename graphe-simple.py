#! /usr/bin/python3.8
"""
    graphe-simple.py
    Created by lwi19
    Copyright © 2020 Louis Plouffe. All rights reserved.
"""

"""
This program explore and show interesting properties in graph theory.
The graphs are simple and undirected.

Modules

Notes       ./graph_theory.note
Main        ./graphe-simple.py
Samples     ./data/some_of_theme.py
Library     ./util/graph_lib.py
Tests       ./tests/graph_test.py

Syntax:
    python3.8 ./graphe-simple.py
Tests:
    python3.8 -m unittest discover  -p "*test.py" -s ./tests  -v

Requirement:
    python 3.8

"""

from data.some_of_them import g_01, g_02, g_03, g_04, g_05, g_06, g_07, g_08
from util.graph_lib import presentation, print_graph, print_adjacency_list


if __name__ == "__main__":
    list_of_graph = [
        g_01,
        g_02,
        g_03,
        g_04,
        g_05,
        g_06,
        g_07,
        g_08,
    ]

    for g in list_of_graph:
        presentation(g)

    # Shortest path test with two random vertices in G_06 random graph.
    if rep := g_06.two_random_vertices():
        vertex_one, vertex_two = rep
        if path := g_06.find_shortest_path(vertex_one, vertex_two):
            print(f"Shortest path from {vertex_one} to {vertex_two} in graph G_06 is length : {len(path) - 1}\n{path=}")
        else:
            print(f"No possible path between {vertex_one} and {vertex_two}")
