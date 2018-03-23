class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                print(nums[i], nums[j], nums[k])
                sum3 = nums[i]+nums[j]+nums[k]
                print(sum3, closest)
                print()
                if sum3==target:
                    return target
                if abs(target-sum3)<abs(target-closest):
                    closest = sum3
                if sum3<target:
                    j += 1
                else:
                    k -= 1
        return closest
            
            