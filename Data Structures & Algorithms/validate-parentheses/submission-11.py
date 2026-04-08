class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}':'{', ')':'(',']':'['}
        open_to_close = {'{':'}','[':']','(':')'}
        open_brackets = ['(','[','{']
        closed_brackets = [')','}',']']

        for c in s:
            if c in open_brackets:
                stack.append(c)
            if c in closed_brackets:
                if not stack:
                    return False
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                elif stack and stack[-1] != close_to_open[c]:
                    return False
            
        return len(stack) == 0
            

        
        