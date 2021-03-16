class Solution:
    def climbStairs(self, n: int) -> int:
      """
      Identical to Fibonacci series (memoizing only last 2 values for O(1) space)
      """
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
            
        return third
