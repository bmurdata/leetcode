# 2/11/21
# Question- https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Is palindrome- stack? On item, pop on,
        # if item is same as top of stack, pop off. 
        # racecar
        
        # Alternatively- make a list of n
        # Idea- make a reverse of the linked list, and 
        # iterate through both. Make head point to null,
        # then iterate over the old list, and make it point to each
        
        if head ==None:
            return True
        prev=head.next
        newTail=ListNode(head.val,None)
        
        while prev != None:
            newNode=ListNode(prev.val,newTail)
            newTail=newNode
            prev=prev.next
        prev=head
        while prev !=None:
            if prev.val != newTail.val:
                return False
            prev=prev.next
            newTail=newTail.next
        return True