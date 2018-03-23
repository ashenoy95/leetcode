class Solution(object):
    def pow(self, x, n):
        if n==0:
            return 1
        if not n%2:
            return self.pow(x*x, n/2)
        else:
            return x*self.pow(x*x,(n-1)/2)
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x
            n = -n
        return self.pow(x, n)
        