# 🌳 `mis` Maximum Independent Set in Trees Python Package

This repository contains one of the possible solutions to the Maximum Independent Set (MIS) problem using dynamic programming. The `max_independent_set` function takes a tree represented as an adjacency list and a root node, and returns the size of the maximum independent set in the tree.

## Implementation

The implementation is partially based on the approach described in "Distributed Algorithms" by Nancy Lynch and general techniques from Dynamic Programming using DFS (Depth-First Search).

## Usage

To use the `max_independent_set` function, first create an adjacency list representation of your tree. For example:

```python
tree = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
```

Then, create a `Graph` object from the adjacency list:

```python
graph = Graph.from_dict(tree)
```

Finally, call the `max_independent_set` function with the graph and the root node to start from:

```python
root = 0
max_set_size = max_independent_set(graph, root)
print("Maximum Independent Set size:", max_set_size)
```

This will output the size of the maximum independent set in the tree.

## Example

The `tests/small_trees_test.py` file contains a test case for a small example tree. You can run the test using the following command:

```sh
pytest tests/small_trees_test.py
```

This will output the size of the maximum independent set for the example tree.
