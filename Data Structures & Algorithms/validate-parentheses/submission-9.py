class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"{" : "}", "[" : "]", "(" : ")"}
        stack = []

        for i in s:
            if i in dictionary:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if dictionary[top] != i:
                        return False
        if stack:
            return False
                    
        return True
