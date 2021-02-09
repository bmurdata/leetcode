# 2/9/21
# Question https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Part of the Feb Challenge
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # Find the largest key value, from there percolate up. Add the higest right tree sum
        # Each node= higest sum of right side. 
        # Left side- parent +self if no children. Else, take its parent add to the most right and 
        # go back up.
        # Post order traversal
        # Visit node- stack?
        # Reverse in order
        # Reverse order- go right, then self, then left. 
        # Running tally?
        # Running sum tally
        
        # Idea: Go backwards, due to property of BST, doing so means each node value is the sum of those
        # visited before it. Need to keep it as self.bigNum so it can be access by member functions.
        self.bigNum=0
        def reverseInorder(node:TreeNode)->TreeNode:
            # If no right side value
            # If right is a tree- return the max value of the node. 
            if not node:
                return 0
            if node != None:
                # print("At node: "+str(node.val))
                x=node.val
                curSum=node.val
                if node.right:
                    reverseInorder(node.right)
                self.bigNum=node.val =self.bigNum+node.val#node.val
                # print("The right side max is something like"+str(self.bigNum))
                print(node.val)
                if node.left:
                    reverseInorder(node.left)
                # print("At node "+str(x)+" we have "+str(node.val))
                return node
            return node
        reverseInorder(root)
        return root