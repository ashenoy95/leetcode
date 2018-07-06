class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True for i in range(n+1)]
        p = 2
        ctr = 0
        
        while p<=n**.5:
            if prime[p]:
                for i in range(2*p, n+1, p):
                    prime[i] = False
                    
            p += 1
            
        for p in range(2, n):
            if prime[p]:
                ctr += 1

        return ctr