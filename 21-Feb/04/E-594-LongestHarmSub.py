# 2/4/21
# Question https://leetcode.com/problems/longest-harmonious-subsequence/

# Longest harmonius Subsequence
test=[1,3,2,2,5,2,3,7]
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Find max and min. If subtraction is ==1
        # Then find the positions of each.
        # Sort arrays of positions. Find the greater of the positions
        # Subtract and return that.
        # Hash maps- looked up solution
        # Key- can remove any number of elements in the array. 
        # Result is ONLY max, or min, with difference of 1
        # Count the max and min and return that result
        # Trick- try hashmap. Think on fundamentals of problem at first
        numDict=dict()
        for i in nums:
            if str(i) in numDict:
                numDict[str(i)] +=1
            else:
                numDict[str(i)]=1
        result=0
        print(numDict)
        for num in numDict:
            oneUp=str(int(num)+1)
            if oneUp in numDict:
                result=max(result,numDict[num]+numDict[oneUp])
        return result

        