class MinStack:

    def __init__(self):
        self.min_elements = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_elements) == 0 or self.min_elements[-1] >= val:
            self.min_elements.append(val)

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.min_elements[-1]:
            self.min_elements.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_elements[-1]
