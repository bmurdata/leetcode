# 2/1/21
# Maximum Subarray
# Question https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Find an O(n) solution
        # Ideally- one pass. 
        # Find the sum of the entire array?
        # Kandane algo and Dynamic programming
        # Hint- smaller problem which can be broken up.
        # Brute force-starting at 0, calculate 
        # sum 0-n,0-n-1....0-0
        # Find max, then continue. 
        if len(nums)==1:
            return nums[0]
        localMax=0
        globalMax=-99999
        for i in range(len(nums)):
            localMax=max(nums[i],nums[i]+localMax)
            if localMax>=globalMax:
                globalMax=localMax
        return globalMax