class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
        else:
            if self.max_stack[-1] < x:
                self.max_stack.append(x)
            else:
                self.max_stack.append(self.max_stack[-1])

    def pop(self) -> int:
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def peekMax(self) -> int:
        if not self.stack:
            return None
        return self.max_stack[-1]

    def popMax(self) -> int:
        res = None
        buffer = []
        while self.stack and self.stack[-1] < self.max_stack[-1]:
            buffer.append(self.stack.pop())
            self.max_stack.pop()
        self.max_stack.pop()
        res = self.stack.pop()
        while buffer:
            self.push(buffer.pop())
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
