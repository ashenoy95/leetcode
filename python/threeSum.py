class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        soln = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                sum3 = nums[i]+nums[j]+nums[k]
                if sum3==0:
                    soln.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j += 1
                    while k>j and nums[k]==nums[k-1]:
                        k -= 1
                if sum3<0:
                    j += 1
                else:
                    k -= 1
        return list(set(map(tuple, soln)))
