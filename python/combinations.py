class Solution(object):
    def comb(self, prefix, l, ctr, final):
        if not ctr:
            final.append(prefix)
            return final
        
        for i in range(len(l)):
            final = self.comb(prefix+[l[i]], l[i+1:], ctr-1, final)
            
        return final
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = [i for i in range(1,n+1)]
        return self.comb([], l, k, [])