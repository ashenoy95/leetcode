class Solution(object):
    def matchPrefix(self, str1, str2):
        i = 0
        j = 0
        prefix = ''
        while i<len(str1) and j<len(str2):
            if str1[i]!=str2[j]:
                break
            prefix += str1[i]
            i += 1
            j += 1
        return prefix
                
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.matchPrefix(prefix, strs[i])
        return prefix
            
        
                
        