# 2/2/21
# Question https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        # Travsers the whole tree, add where the number is >=low
        # and <=high
        finalSum=0
        def traverseTree(node,finalSum):
            if node is None:
                return finalSum
            elif node.val>=low and node.val<=high:
                print(node.val)
                finalSum+=node.val
            # Traverse
            if node.right !=None and node.left!=None:
                finalSum +=traverseTree(node.left,0)
                finalSum+= traverseTree(node.right,0)
            
            elif node.right != None:
                finalSum+=traverseTree(node.right,0)
            elif node.left != None:
                finalSum+=traverseTree(node.left,0)
            return finalSum
        finalSum=traverseTree(root,finalSum)
        
        return finalSum