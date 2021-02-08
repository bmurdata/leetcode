# 2/7/21

# Question https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # For each character, measure backwards and forwards, 
        # Wait....get index of where each occurance of c is
        # For each location of c, go right to left. 
        # Iterate through, when find first occurance of c, go backwards and count. 
        # Then continue and add 1 to each dist. when find next, go backwards.
        
        # Initialize array of 0
        res=[ len(s) for i in range(len(s)) ]

        
        prev=-1
        countForward=0
        foundC=False
        for x in range(len(s)):
            countForward+=1
            if foundC:
                res[x] =countForward
            
            current=x
            
            # Go backwards from c
            if s[x]==c:
                foundC=True
                print(str(x) +" Hit C at there going back to "+str(prev))
                countBack=-1
                res[x]=0
                for i in range(x,prev,-1):
                    countBack +=1
                    if res[i]>countBack:
                        print(res[i])
                        res[i]=countBack
                    if i==0:
                        res[i]=countBack
                countForward=0
                prev=x
            
        return res
        
        