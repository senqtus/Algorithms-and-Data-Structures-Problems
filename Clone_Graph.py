"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
"""
from collections import deque


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    @staticmethod
    def clone_graph(root: 'Node') -> 'Node':
        """
        :param root: root node of original tree
        :return: root of cloned tree
        """

        def bfs(node: 'Node', visited: 'dict') -> 'None':
            """
            :param node: current working node
            :param visited: dict where key is node from original tree, value is equivalent node in cloned tree
            :return: None
            """
            queue = deque()
            queue.append(node)
            while queue:
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        new_node = Node(neighbor.val, [])
                        visited[neighbor] = new_node
                    visited[node].neighbors.append(visited[neighbor])

        cloned_root = Node(root.val, [])
        cloning_dictionary = dict()
        cloning_dictionary[root] = cloned_root
        bfs(root, cloning_dictionary)
        return cloned_root