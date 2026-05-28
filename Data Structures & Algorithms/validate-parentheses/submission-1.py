class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                p_stack.append(c)
                continue
            elif c == ']':
                if len(p_stack) == 0: return False
                if p_stack.pop() != '[':
                    return False
            elif c == '}':
                if len(p_stack) == 0: return False
                if p_stack.pop() != '{':
                    return False
            elif c == ')':
                if len(p_stack) == 0: return False
                if p_stack.pop() != '(':
                    return False
        return len(p_stack) == 0