# 2/10/21
# Question https://leetcode.com/problems/copy-list-with-random-pointer/solution/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    self.hashmap_Visited={}
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Job-recreate the list. Why? Iterate through the list, and set. Use while loop, time 
        # complexity is O(n)
        # Looked at hints- doesn't the interweaving break the idea? I thought nothing could point to
        # the old list! Using it regardless. 
        newHead=Node
        if head !=None:
            # DO NOT point to any original items in the list. at the end
            head.next
            newHead=Node(head.val,None,None)
            prev=head
            newprev=newHead
            while prev !=None:
                if prev.next !=None:
                    
                    newprev.next=Node(prev.next.val,None,None)
                newprev=newprev.next
                prev=prev.next
            
            # New List made. Iterate both lists, use head.random val
            
            # if head.next !=None:
            #    newHead.next=head.next

            prev=head
            # Plan- iterate through and create copies of the node at each junction. Ignore random
            # For random-first go back starting at newHead, compare to old list. 
            # OH now I kind of understand the interweave- set it equal to the pointer
            
        else:
            return None
        return newHead