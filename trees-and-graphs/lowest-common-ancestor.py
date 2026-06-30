class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def first_common_ancestor(root,p,q):

    # base case
    if root is None:
        return None
    if root == p or root == q:
        return root
    
    # recursively search on left side
    left = first_common_ancestor(root.left,p,q)
    right = first_common_ancestor(root.right,p,q)

    # if both side returns a node , current node is LCA
    if left and right:
        return root
    
    # otherwise return non null node
    return left if left else right

A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
G = TreeNode("G")
H = TreeNode("H")

A.left = B
A.right = C
B.left = D
B.right = E
E.left = G
E.right = H

ancestor = first_common_ancestor(A, G, H)
print(ancestor.val)