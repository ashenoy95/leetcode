class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]*i for i in range(1, numRows+1)]
        
        for i in range(numRows):
            for j in range(i+1):
                if i==j or j==0:
                    continue
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
                    
        return pascal