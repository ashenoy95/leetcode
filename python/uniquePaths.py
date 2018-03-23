class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        OPT = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                OPT[i][j] = OPT[i-1][j] + OPT[i][j-1]
        return OPT[m-1][n-1]