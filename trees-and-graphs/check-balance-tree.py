class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):
    def dfs(node):
        if not node:
            return [True,0]     # true mean , this is balanced and with height of the current node
        
        left,right = dfs(node.left),dfs(node.right)
        isBalanced = left[0] and right[0] and abs(left[1]-right[1]) <=1

        return [isBalanced,1+max(left[1],right[1])]
    
    return dfs(root)[0]
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(14)

print(is_balanced(root))