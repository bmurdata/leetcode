# 2/3/20
# Question https://leetcode.com/problems/valid-parentheses/

test="()"

class Solution:
    def isValid(self, s: str) -> bool:
        # STACK!!!!
        # If opening, put onto the stack
        # If closing and if matches opening, pop off
        # If at end enpty, return true
        
        # Arrays first then dictionary
        stack=list()
        rights=['(','{','[']
        lefts=[')','}',']']
        for i in s:
            if i in rights:
                stack.append(i)
            else:
                # Matching parentesis
                if(len(stack)==0):
                    return False
                if rights.index(stack[len(stack)-1]) == lefts.index(i):
                    stack.pop()
                else:
                    return False
                    
        if len(stack) ==0:
            return True
        return False

print(Solution.isValid(test))