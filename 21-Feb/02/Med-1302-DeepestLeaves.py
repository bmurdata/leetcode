# 2/2/21
# Question https://leetcode.com/problems/deepest-leaves-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # DFS go down the left, all the way down in both directions.
        # Find the max depth of both sides. 
        alldepths=list()
        deepestnodes=list()
        def findDepth(parent:TreeNode,node:TreeNode,depth:int):
            if not node:
                deepestnodes.append(parent)
                return depth
            if node.right !=None and node.left != None:
                alldepths.append(findDepth(node,node.left,depth+1))
                alldepths.append(findDepth(node,node.right,depth+1))
            elif node.left !=None:
                alldepths.append(findDepth(node,node.left,depth+1))
            elif node.right !=None:
                alldepths.append(findDepth(node,node.right,depth+1))
            elif node.right ==None and node.left == None:
                deepestnodes.append([node.val,depth])
            return depth
        
        findDepth(root,root,0)
        depths=max(alldepths)
        result =0
        for i in deepestnodes:
            if i[1]==depths:
                result += i[0]
        return result