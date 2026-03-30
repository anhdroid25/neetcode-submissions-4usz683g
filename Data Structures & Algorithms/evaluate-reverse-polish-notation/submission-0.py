class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators =  {"+", "-", "*", "/"}
        for i in tokens:
            if  i in operators:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    result = first + second
                    stack.append(result)
                elif i == "-":
                    result = second - first
                    stack.append(result)
                elif i == "*":
                    result = (first * second)
                    stack.append(result)
                elif i == "/":
                    result = int(second / first)
                    stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]

