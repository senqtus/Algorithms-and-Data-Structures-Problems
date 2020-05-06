"""
You are given the root of a binary search tree.
Return true if it is a valid binary search tree,
and false otherwise. Recall that a binary search tree
has the property that all values in the left subtree
are less than or equal to the root, and all values in the right subtree
are greater than or equal to the root.

Here's a starting point:
"""


class TreeNode:
    def __init__(self, key: 'int'):
        self.key = key
        self.left = None
        self.right = None


def get_validation(nums: 'list') -> 'bool':
    for index in range(1, len(nums)):
        if nums[index - 1] >= nums[index]:
            return False
    return True


def is_bst(root: 'TreeNode') -> 'bool':
    nums = []

    def inorder(node: 'TreeNode'):
        if node is not None:
            inorder(node.left)
            nums.append(node.key)
            inorder(node.right)

    inorder(root)
    isValid = get_validation(nums)
    return isValid


if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
# 1  4 6
