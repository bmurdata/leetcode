class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force- for each character, check if in string.
        
        # If different lengths, must be false
        # Problem with proposed brute force-what if aaa vs aab? Dictionary solves it
        
        
        if len(s) !=len(t):
            return False
        sDict={}
        
        for letter in s:
            if letter in sDict:
                sDict[letter] +=1
            else:
                sDict[letter]=1
        for key in sDict:
            if t.count(key) !=sDict[key]:
                return False
        return True