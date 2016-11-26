# Notes

## Knapsack Problem
* Brute Force:
 * сгенерировать все возможные комбинации (power set)
 * удалить те, в которых сумарный вес больше, чем разрешенный вес
 * из остальных комбинаций выбрать ту, вес которой самый большой
* Greedy algorithm
 * пока рюкзак не заполнен, добавлять лучший элемент
* Search tree
 * left-first, depth-first


## Dynamic programming

![Call tree for recursive fibonacci](https://upload.wikimedia.org/wikibooks/en/3/37/Algorithms-F6CallTree.png)

__memoization__ - сохранение результатов выполнения функции.


## Graph

* nodes (vertices)
* edges (arcs)

* Undirected (graph)
* Directed (digraph)
* Unweighted or weighted

Tree:
* A directed graph in which each pair of nodes is connected by a single path


Representations:
* Adjacency matrix
* Adjacency list

Shortest path:
* Depth-first search (DFS)
* Breadth-first search (BFS)


Weighted Shortest Path
* DFS
