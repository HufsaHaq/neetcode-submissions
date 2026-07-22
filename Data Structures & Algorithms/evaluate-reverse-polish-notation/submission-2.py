class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']

        # could use a stack 
        # keep on adding until reach an operation

        stack = []

        for i in tokens:
            if i in ops:
                term2 = stack.pop()
                term1 = stack.pop()
                if i == '*':
                    stack.append(term1*term2)
                if i == '-':
                    stack.append(term1-term2)
                if i == '+':
                    stack.append(term1+term2)
                if i == '/':
                    stack.append(int(term1/term2))
            else:
                stack.append(int(i))
        
        return int(stack[0])