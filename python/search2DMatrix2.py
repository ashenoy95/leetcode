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
        for row in matrix:
            if self.binarySearch(row, 0, len(row)-1, target):
                return True
        return False