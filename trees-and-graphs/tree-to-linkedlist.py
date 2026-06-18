from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_level_linked_lists(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        dummy = ListNode(0)
        current = dummy

        for _ in range(level_size):
            node = queue.popleft()

            current.next = ListNode(node.val)
            current = current.next

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(dummy.next)

    return result

def print_lists(lists):
    for depth, head in enumerate(lists):
        print(f"Depth {depth}:", end=" ")

        current = head
        while current:
            print(current.val, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next

        print()
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

lists = create_level_linked_lists(root)
print_lists(lists)

""" Time complexity will be O(N) 
    Because we visit every node once
"""