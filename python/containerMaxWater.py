class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        max_area = max{min{height[i], height[j]} * (j - i)}
        i.e. we want to maximize min(height[i], height[j]) & maximize (j - i)
        to maximize j - i, we start with i & j at 2 ends
        increment/decrement i & j respectively in order to maximize min{height[i], height[j]}
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            max_area = max(area, max_area)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return max_area
    
