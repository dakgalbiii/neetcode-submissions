class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        # 1 2 + 3 * 4 -
        # 1 + 2
        # (1 + 2) * 3
        # ((1 + 2) * 3) - 4
        # every time we encounter a new operation,
        # we want to parenthesize what we have curerntly
        # otherwise, we push numbers onto the stack

        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                val = 0
                if t == '+':
                    val += num1 + num2
                elif t == '-':
                    val += (num1 - num2)
                elif t == '*':
                    val += (num1 * num2)
                else:
                    val += int(num1 / num2)
                stack.append(val)
            else:
                stack.append(int(t))
        return stack[-1]