class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(14)

print(is_balanced(root))