'''
You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

Here's your starting point:
'''


class Node(object):
    def __init__(self, value: 'int', next_element: 'Node' = None):
        self.val = value
        self.next = next_element

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge_two_lists(first_node: 'Node', second_node: 'Node') -> 'Node':
    current = Node(0)
    root = current

    while True:

        if first_node is None:
            current.next = second_node
            break
        if second_node is None:
            current.next = first_node
            break

        if first_node.val <= second_node.val:
            current.next = first_node
            current = current.next
            first_node = first_node.next
        else:
            current.next = second_node
            current = current.next
            second_node = second_node.next

    return root.next


def merge_linked_lists(lists: 'list') -> 'list':
    if not lists:
        return None
    from_index = 0
    to_index = len(lists) - 1

    while to_index > 0:
        left = from_index
        right = to_index
        while left < right:
            lists[left] = merge_two_lists(lists[left], lists[right])
            left += 1
            right -= 1
        to_index = right
    return lists[0]


if __name__ == '__main__':
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    c = Node(2, Node(4, Node(6)))
    print(merge_linked_lists([a, b, c]))
    # 123456
