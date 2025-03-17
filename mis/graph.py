from __future__ import annotations
from ast import Eq
from dataclasses import dataclass

@dataclass
class Edge:
    u: int
    v: int

    def __hash__(self):
        if self.u > self.v:
            return hash((self.v, self.u))
        else:
            return hash((self.u, self.v))

@dataclass
class Graph:
    nodes: set[int]
    edges: set[Edge]

    @staticmethod
    def from_dict(edges: dict[int, list[int]]) -> Graph:
        nodes = set(edges.keys())
        edges_set = set()
        neighbors = [[] for _ in range(len(nodes))]

        for u, v in edges.items():
            for w in v:
                edges_set.add(Edge(u, w))

        return Graph(nodes, edges_set)
