class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = {word:None for word in wordDict} # converting to dict for efficient lookup
        OPT = [False for i in range(len(s)+1)]
        OPT[0] = True   # base case
        
        for j in range(1, len(s)+1):
            for i in range(j):
                #print(s[i:j+1])
                if s[i:j] in wordDict and OPT[i]:
                   #print('{} exists'.format(s[i:j]))
                    OPT[j] = True
                #print(OPT)
            #print()
        
        return OPT[-1]