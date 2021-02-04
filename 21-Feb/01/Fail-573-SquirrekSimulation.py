# 2/1/21 
# Squirrel Simulations
# Question https://leetcode.com/problems/squirrel-simulation/
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # Tree= home base, tuple of 2
        # Squirrel- can move around and grab nuts.
        # Nuts- array of X,Y points with n nuts
        
        # Assumption- Optimal for the squirrel to get the closest Nut first, then bring to the tree
        # From tree go to closest nut, and keep going until all cleared.
        # To find the first nut, find min( [abs(squirrel[0]-nut[0])+ abs(squirrel[1]-nut[1]) for nut in nuts])
        # From there find distance to first nut. 
        
        # print([abs(squirrel[0]-nut[0])+ abs(squirrel[1]-nut[1]) for nut in nuts])
        
        mint=max([abs(tree[0]-nut[0])+ abs(tree[1]-nut[1]) for nut in treemin])
        minsq=min([abs(squirrel[0]-nut[0])+ abs(squirrel[1]-nut[1]) for nut in nuts])
        
        
        
        treemin= list()
        
        print("We have "+str(len(nuts)))
        for nut in nuts:
            if abs(squirrel[0]-nut[0])+ abs(squirrel[1]-nut[1]) ==result:
                print("Found a min: ")
                print(nut)
                treemin.append(nut)
                
        mintree= max([abs(tree[0]-nut[0])+ abs(tree[1]-nut[1]) for nut in treemin])
        result +=mintree
        print("R    esult is bull shit "+str(result))
        for nut in treemin:
            if abs(tree[0]-nut[0])+ abs(tree[1]-nut[1]) ==mintree:
                print("Found a min from the tree: ")
                print(nut)
                nuts.remove(nut)
                break
        
        print("We have "+str(len(nuts)))
        print ([abs(tree[0]-nut[0])+ abs(tree[1]-nut[1]) for nut in nuts])
        count=0
        print(nuts)
        
        for mindist in [abs(tree[0]-nut[0])+ abs(tree[1]-nut[1]) for nut in nuts]:
            count += mindist
            result += (mindist*2)
        print(count)
        return result
            
            