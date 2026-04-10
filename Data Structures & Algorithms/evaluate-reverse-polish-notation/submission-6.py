class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    result = first + second
                    stack.append(result)
                if i == "*":
                    result = first * second
                    stack.append(result)
                if i == "-":
                    result = second - first
                    stack.append(result)
                if i == "/":
                    result = int(second/first)
                    stack.append(result)
        return stack[0]
