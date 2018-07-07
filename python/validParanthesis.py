from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        valid = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if stack and stack.pop()==valid[char]:
                    continue
                else:
                    return False
        
        return not stack