class Solution(object):    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = 0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                flag = 1
                break
        if flag==0:
            return s
        
        OPT = [[False for i in range(len(s))] for j in range(len(s))]
        longest = 0
        start = 0
        end = 0
        
        for i in range(len(s)):
            for j in range(len(s)):
                if i==j:
                    OPT[i][j] = True
                if j==i+1:
                    OPT[i][j] = s[i]==s[j]
                if OPT[i][j]:
                    if j-i+1>longest:
                        longest = j-i+1
                        start = i
                        end = j+1
                        
        for j in range(2, len(s)):
            for i in range(j-1):
                if OPT[i+1][j-1] and s[i]==s[j]:
                    OPT[i][j] = True
                    if j-i+1>longest:
                        longest = j-i+1
                        start = i
                        end = j+1
                        
        return s[start:end]

