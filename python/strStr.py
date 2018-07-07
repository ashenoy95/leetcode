class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        i = 0
        j = 0
        k = 0
        
        while i<len(haystack) and j<len(needle): 
            if needle[j]==haystack[i]:
                j += 1
                i += 1
            else:
                j = 0
                k += 1
                i = k
                
            if j==len(needle):
                return i-j
            
        return -1