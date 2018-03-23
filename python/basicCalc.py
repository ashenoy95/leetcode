class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack1 = []
        stack2 = []
        operators = {'+':2, '-':2, '(':1, ')':1}
        temp = ''

        for char in s:
            if char==' ':
                continue
            
            if char not in operators:
                temp += char
            else:
                if temp:
                    stack1.append(temp)
                    temp = ''
                if char=='(':
                    stack2.append('(')
                    
                elif char==')':
                    while stack2[-1]!='(':
                        op = stack2.pop()
                        op2 = int(stack1.pop())
                        op1 = int(stack1.pop())
                        if op=='+':
                            stack1.append(op1+op2)
                        else:
                            stack1.append(op1-op2)
                    stack2.pop()
                else:    
                    while stack2 and operators[stack2[-1]]>=operators[char]:
                        op = stack2.pop()
                        op2 = int(stack1.pop())
                        op1 = int(stack1.pop())
                        if op=='+':
                            stack1.append(op1+op2)
                        else:
                            stack1.append(op1-op2)
                    stack2.append(char)

        if temp:
            stack1.append(temp)

        while stack2:
            op = stack2.pop()
            op2 = int(stack1.pop())
            op1 = int(stack1.pop())
            if op=='+':
                stack1.append(op1+op2)
            else:
                stack1.append(op1-op2)

        return int(stack1[-1])
                
        
        
