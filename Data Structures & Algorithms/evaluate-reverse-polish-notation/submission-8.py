class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # General Idea: 
        # Add numbers to the stack. When you find an operator, apply the opterator to the 
        # last 2 numbers (pop them) then add the new result into the stack

        stack = []
        for token in tokens:
            # is numeric does not work for negative values
            try:
                stack.append(int(token))
            except:
                y = stack.pop()
                x = stack.pop()
                num = self.compute(x, y, token)
                stack.append(num)
        print(stack)

        return stack[0]
    def compute(self, a, b, operation: str):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return int(a / b)

        return None