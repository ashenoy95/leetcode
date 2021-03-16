class Solution:
    """
    3Sum wraps 2Sum in an outer loop, similarly 4Sum can be built up as 3Sum wrapped in another
    loop. This can be generalized to kSum using k-2 loops over 2Sum. 
    Time: O(n^(k-1))
    Space: O(n) for recursion stack
    Reference: https://leetcode.com/problems/4sum/solution/
    """
    def twoSum(self, nums, target):
        result = []
        i = 0
        j = len(nums) - 1
        
        while i < j:
            s = nums[i] + nums[j] 
            
            if (s > target) or ((j < len(nums) - 1) and (nums[j] == nums[j+1])):
                j -= 1
            elif (s < target) or ((i > 0) and (nums[i] == nums[i-1])):
                i += 1
            else:
                result.append([nums[i], nums[j]])
                i += 1
                j -= 1
        
        return result
    
    
    def kSum(self, nums, target, k):
        result = []
        if (not nums) or (sum(nums[:k]) > target) or (sum(nums[-k:]) < target):
            return []
        
        if k == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
                
            k_minus_sums = self.kSum(nums[i+1:], target-nums[i], k-1)
            for s in k_minus_sums:
                result.append([nums[i]] + s)
    
        return result
        
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, k=4)
    
