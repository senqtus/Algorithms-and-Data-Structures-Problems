"""
Given an integer k and a binary search tree,
find the floor (less than or equal to) of k,
and the ceiling (larger than or equal to) of k.
If either does not exist, then print them as None.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def finding_floor(self, root_node: 'Node', k: 'int') -> 'Node':
        """
        :param root_node: root of subtree
        :param k: value for which we are looking for floor
        :return: node in BST which has value less or equal to k
        """
        if root_node is None:
            return None
        if root_node.value == k:
            return root_node
        elif k < root_node.value:
            # left subtree answer
            return self.finding_floor(root_node.left, k)

        right_subtree_answer = self.finding_floor(root_node.right, k)
        if right_subtree_answer is None:
            return root_node
        return right_subtree_answer

    def finding_ceiling(self, root_node: 'Node', k: 'int') -> 'Node':
        """
        :param root_node: root of subtree
        :param k: value for which we are looking for floor
        :return: node in BST which has value more or equal to k
        """
        if root_node is None:
            return None
        if root_node.value == k:
            return root_node
        elif k > root_node.value:
            # right subtree answer
            return self.finding_ceiling(root_node.right, k)

        left_subtree_answer = self.finding_ceiling(root_node.left, k)
        if left_subtree_answer is None:
            return root_node
        return left_subtree_answer


def build_bst() -> 'Node':
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)
    return root


if __name__ == '__main__':
    root = build_bst()
    print([root.finding_ceiling(root, 5).value, root.finding_floor(root, 5).value])
