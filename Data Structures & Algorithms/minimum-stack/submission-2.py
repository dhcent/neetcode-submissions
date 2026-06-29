import math
class MinStack:
    # when adding elements, always keep track of min
    def __init__(self):
        self.stack = []
        self.min_history = [math.inf]


    def push(self, val: int) -> None:
        self.stack.append(val)
        # Constantly update the current min
        if val <= self.min_history[-1]:
            self.min_history.append(val)

    # could just use generic pop implementation but I want to create one my self.
    def pop(self) -> None:
        temp = self.stack.pop()
        if self.min_history[-1] == temp:
            self.min_history.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_history[-1]