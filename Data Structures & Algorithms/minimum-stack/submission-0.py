class MinStack:

    def __init__(self):
        self.stack = [] #index 0 is at bottom
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        

    def pop(self) -> None:
        print(self.stack)
        self.stack.pop(-1)
        print(self.stack)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

