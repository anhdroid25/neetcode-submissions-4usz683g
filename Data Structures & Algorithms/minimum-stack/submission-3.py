class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)
        if not self.minstack or val <= self.minstack[0]:
            self.minstack.insert(0, val)

    def pop(self) -> None:
        if self.stack[0] == self.minstack[0]:
            self.minstack.pop(0)
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minstack[0]
        
