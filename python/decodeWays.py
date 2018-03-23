class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        OPT = [0 for i in range(len(s)+1)]
        OPT[0] = 1
        OPT[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1:i])>0 and int(s[i-1:i])<10:
                OPT[i] += OPT[i-1]
            if int(s[i-2:i])>9 and int(s[i-2:i])<=26:
                OPT[i] += OPT[i-2]
        return OPT[-1]