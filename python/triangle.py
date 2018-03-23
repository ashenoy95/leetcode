class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        OPT = [num for num in triangle[-1]]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                OPT[j] = min(OPT[j], OPT[j+1]) + triangle[i][j]
        return OPT[0]