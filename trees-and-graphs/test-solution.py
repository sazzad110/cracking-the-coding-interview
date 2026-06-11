# test.py
from solution import Solution

def inorder_traversal(root):
    """Helper to print inorder traversal of BST."""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

if __name__ == "__main__":
    # Initialize a sorted array
    nums = [1, 2, 3, 4, 5, 6, 7]

    # Create BST
    sol = Solution()
    root = sol.sortedArrayToBST(nums)

    # Print inorder traversal (should match original array)
    print("Input array:", nums)
    print("Inorder traversal of BST:", inorder_traversal(root))
