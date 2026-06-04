class MinStack:
    def __init__(self):
        self.currentMin = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.currentMin = min(val, self.stack[-1][1] if self.stack else float('inf'))
        self.stack.append((val, self.currentMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]