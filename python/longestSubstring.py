class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        chars = {}
        longest = 0
        
        for j in range(len(s)):
            if s[j] in chars:
                # reason for max(): if first occurence of a char is before current left ptr i
                # e.g.: if 'a' is at i=0 & a different char is repeated between 1 <= i < n, i > 1
                # now, if 'a' is repeated, i should not be set as 1, rather max(1, i)
                i = max(chars[s[j]], i)
                
            chars[s[j]] = j + 1
            longest = max(longest, j - i + 1)

        return longest
