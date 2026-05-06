class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (token in "+-*/"):
                a = int(stack[-2])
                b = int(stack[-1])
                stack.pop()
                stack.pop()
                if token == "+":
                    stack.append(str(a + b))
                elif token == "-":
                    stack.append(str(a - b))
                elif token == "*":
                    stack.append(str(a * b))
                elif token == "/":
                    stack.append(str(int(a / b)))
            else:
                stack.append(token)
        return int(stack[0])
                
                 
