class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #keep track of opening brackets
        #match closing to opening
        closetoopen = {")" : "(","]" : "[", "}" : "{" }

        for i in s:
            if i in closetoopen: #if it is closing brackets
                #check if stack is not empty and the top matches the opening bracket
                if stack and stack[-1] == closetoopen[i]:
                    stack.pop() #remove matching opening bracket from stack
                else:
                    return False #mismatch or empty stack
            else:
                stack.append(i) #if opening bracket, push to stack
        #if stack is empty, all brackets match correctly
        return True if not stack else False
