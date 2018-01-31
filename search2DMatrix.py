class Solution(object):
    def binarySearch(self, arr, left, right, target):
        if left>right:
            return False
        mid = (left+right)//2
        if arr[mid]==target:
            return True
        elif target<arr[mid]:
            return self.binarySearch(arr, left, mid-1, target)
        else:
            return self.binarySearch(arr, mid+1, right, target)
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        firstCol = [row[0] for row in matrix]
        for i in range(len(firstCol)):
            if target==firstCol[i]:
                return True
            if i+1<len(firstCol) and target>firstCol[i] and target<firstCol[i+1]:
                break
        return self.binarySearch(matrix[i], 0, len(matrix[i])-1, target)
        
        
        