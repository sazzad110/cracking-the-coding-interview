""" Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a 
    binary search tree. You may assume that each node has a link to its parent. 
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def inorder_successor(node):
    if not node:
        return None
    
    # Case 01: Node has right sub-tree
    # Logic. : Go to the right once, then keep going left as much as possible
    if node.right:
        curr = node.right

        while curr.left:
            curr = curr.left
        
        return curr
    
    # Case 02: Node has no right sub-tree
    # Logic  : The successor must be one of its ancestors. Keep moving up while the current node is a right child of its parent if you got
    # a parent where you come from left side then stop and return that node
    curr = node
    while curr.parent and curr == curr.parent.right:
        curr = curr.parent

    return curr.parent 

root = TreeNode(20)

root.left = TreeNode(10)
root.left.parent = root

root.right = TreeNode(30)
root.right.parent = root

root.left.left = TreeNode(5)
root.left.left.parent = root.left

root.left.right = TreeNode(15)
root.left.right.parent = root.left

root.left.right.left = TreeNode(13)
root.left.right.left.parent = root.left.right

root.left.right.right = TreeNode(17)
root.left.right.right.parent = root.left.right

root.right.left = TreeNode(25)
root.right.left.parent = root.right

root.right.right = TreeNode(35)
root.right.right.parent = root.right


print(inorder_successor(root.left).val)              # 13
print(inorder_successor(root.left.right).val)        # 17
print(inorder_successor(root.left.right.right).val)  # 20
print(inorder_successor(root.right.right))           # None