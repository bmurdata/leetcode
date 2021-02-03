# 2/2/21
# Question 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # BST- tree node, Lowest on the left, highest right, while not null
        
        # Remove out of range for highest and lowest. Stack?
        # For root: if Higher than Highest, remove all the items to the right
        # If lower, remove all items to the left and itself. Set root=right
        # If root is in range- know that left is not higher. Test against lowest
        # Likewise, for right test against highest.
        # For each node, 
        # Add to stack, and remove going left, then right.
        # Visit all nodes, 
        # Recursion
        # If higher and left is there
        
        def trimm(node:TreeNode):
            if not node:
                return None
            elif node.val>high:
                return trimm(node.left)
            elif node.val<low:
                return trimm(node.right)
            else:
                node.right=trimm(node.right)
                node.left=trimm(node.left)
                return node
        return trimm(root)


# Weirdly better running solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # Neeed function to visit nodes
        # Intiution- recursion. If val of node is higher, remove entire
        # Right side. Focus on left. Vice versa for lower.
        # Visit the node
        def visit(node):
            if not node:
                print("No node here!")
                return None
            elif node.val>high:
                node=visit(node.left)
            elif node.val<low:
                node=visit(node.right)
            else:
                node.right=visit(node.right)
                node.left=visit(node.left)
            return node
        print("Visiting root node")
        return visit(root)
        