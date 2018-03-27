class Solution {
    public boolean binarySearch(int[] arr, int target, int left, int right) {        
        if(left>right)
            return false;
        
        int mid = (left + right)/2;
        
        if(arr[mid]==target) {
            return true;
        } else if(arr[mid]>target) {
            return binarySearch(arr, target, left, mid-1);
        } else {
            return binarySearch(arr, target, mid+1, right);
        }
    }
    
    public boolean searchMatrix(int[][] matrix, int target) {  
        
        if(matrix.length<1 || matrix[0].length<1)
            return false;
    
        int i = 0, j = matrix[0].length-1;
        
        while(i<matrix.length && j>=0) {
            if(matrix[i][j]==target) {
                return true;
            }
            if(matrix[i][j]>target) {
                j--;
            } else {
                i++;
            }
        }
        /* O(nlog n) 
        for(int[] row: matrix) {
            if(binarySearch(row, target, 0, row.length-1))
                return true;
        }
        */
        return false;
    }
}