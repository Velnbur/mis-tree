"""
This module provides an implementation of the Maximum Independent Set (MIS) problem using dynamic programming.

The `max_independent_set` function takes a tree represented as an adjacency list and a root node, and returns
the size of the maximum independent set in the tree.

Implementation is taken from "Distributed Algorithms" by Nancy Lynch and recursive DNF algorithm.
"""

from mis.graph import Graph

def max_independent_set(graph: Graph, root: int) -> int:
    """
    Returns the size of the maximum independent set in the graph.
    """

    # Initialize DP arrays
    dp_incl = {node: 0 for node in graph.nodes}
    dp_excl = {node: 0 for node in graph.nodes}

    def dfs(node: int, parent: int) -> None:
        dp_incl[node] = 1  # If we include the node
        dp_excl[node] = 0  # If we exclude the node

        for edge in graph.edges:
            if edge.u == node:
                child = edge.v
                if child != parent:
                    dfs(child, node)
                    dp_incl[node] += dp_excl[child]
                    dp_excl[node] += max(dp_incl[child], dp_excl[child])

    # Start DFS from the root
    dfs(root, -1)

    # The result is the maximum of including or excluding the root
    result = max(dp_incl[root], dp_excl[root])
    return result
