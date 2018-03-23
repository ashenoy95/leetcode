class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        flag = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    flag = 1
        OPT = [[0]*len(matrix[0]) for i in range(len(matrix))]
        m = 0
        for i in range(len(matrix[0])):
            OPT[0][i] = int(matrix[0][i])
        for i in range(len(matrix)):
            OPT[i][0] = int(matrix[i][0])
        for i in range(1,len(OPT)):
            for j in range(1,len(OPT[0])):
                if int(matrix[i][j])+int(matrix[i-1][j])+int(matrix[i-1][j-1])+int(matrix[i][j-1])==4:
                    if OPT[i-1][j]>=4 and OPT[i-1][j-1]>=4 and OPT[i][j-1]>=4:
                        OPT[i][j] = int((min(OPT[i-1][j], OPT[i-1][j-1], OPT[i][j-1])**.5 + 1)**2)
                    else:
                        OPT[i][j] = 4
                else:
                    OPT[i][j] = 0
                if OPT[i][j]>m:
                    m = OPT[i][j]
        return max(m, flag)
            