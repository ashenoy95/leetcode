class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        i = 0
        min_len = len(nums) + 1
        
        for j in range(len(nums)):
            s += nums[j]
            
            while s >= target:
                min_len = min(min_len, j - i + 1)
                s -= nums[i]
                i += 1
                
        if min_len > len(nums):
            return 0
        else:
            return min_len
        
