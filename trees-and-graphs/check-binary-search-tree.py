class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isValidBst(root):
    def valid(node,low,high):
        if node is None:
            return True
        
        if not (low<node.val and high>node.val):
            return False
        
        return ( valid(node.left,low,node.val) and valid(node.right,node.val,high))
    
    return valid(root,float("-inf"),float("inf"))

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

print(isValidBst(root))