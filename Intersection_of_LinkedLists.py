"""
You are given two singly linked lists. The lists intersect at some node. Find, and return the node.
Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4

This should return 3 (you may assume that any nodes with the same value are the same node).

Here is a starting point:
"""


class Node:
    def __init__(self, value: 'int', next_element: 'Node' = None):
        self.value = value
        self.next = next_element


def get_length(node: 'Node') -> 'int':
    length = 0
    while node is not None:
        length += 1
        node = node.next
    return length


def traverse(node: 'Node', length: 'int'):
    while length > 0 and node is not None:
        length -= 1
        node = node.next
    return node


def are_intersected(node_a, node_b) -> 'bool':
    while node_a.next is not None:
        node_a = node_a.next
    while node_b.next is not None:
        node_b = node_b.next
    return node_a == node_b


def intersection(first: 'Node', second: 'Node') -> 'Node':
    if first is None or second is None or not are_intersected(first, second):
        return None
    length_a = get_length(first)
    length_b = get_length(second)
    if length_a > length_b:
        first = traverse(first, length_a - length_b)
    else:
        second = traverse(second, length_b - length_a)

    while first != second:
        first = first.next
        second = second.next
    return first


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        current = self
        string = ''
        while current is not None:
            string += str(current.val) + '->'
            current = current.next
        string += 'None'
        return string


if __name__ == '__main__':
    first = Node(1)
    first.next = Node(2)
    first.next.next = Node(3)
    first.next.next.next = Node(4)

    second = Node(6)
    second.next = first.next.next

    c = intersection(first, second)
    print(c)
