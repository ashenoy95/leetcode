class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = [0 for m in range(len(matrix))]
        cols = [0 for n in range(len(matrix[0]))]
        
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if not matrix[m][n]:
                    rows[m] = 1
                    cols[n] = 1
                    
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if rows[m] or cols[n]:
                    matrix[m][n] = 0
                    