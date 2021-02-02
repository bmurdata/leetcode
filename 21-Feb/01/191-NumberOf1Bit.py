# 2/1/21
# Number of 1 bits
# Question- https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')