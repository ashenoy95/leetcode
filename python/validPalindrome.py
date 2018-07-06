import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+', '', s).lower()
        
        i = 0
        j = len(s)-1
        
        while i<len(s) and j>=0:
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        
        return True