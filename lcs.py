class Solution(object):    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        temp = 0
        l = 0
        i = 0
        while (i<len(s)):
            if s[i] not in hashmap: 
                hashmap[s[i]] = i
                temp += 1
                i += 1
            else:
                j = hashmap[s[i]]
                i = j+1
                hashmap = {}
                if temp>l:
                    l = temp
                temp = 0
        return max(temp, l)
                                     
                
                