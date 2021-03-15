class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        aux_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                # print(stack)
            elif s[i] == ')':
                if not stack:
                    aux_stack.append(i)
                else:
                    stack.pop()

        
        s_valid = ''.join([s[i] for i in range(len(s)) if i not in (stack + aux_stack)])
        return s_valid
    
