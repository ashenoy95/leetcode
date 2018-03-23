class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        for i in range(len(s)):
            if chars[s[i]]==1:
                return i
        return -1