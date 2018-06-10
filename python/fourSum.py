class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sums = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = nums[i]+nums[j]
                if s not in sums:
                    sums[s] = [[i, j]]
                else:
                    sums[s].append([i, j])
                
        soln = []
        # print('target:', target)
        # print(nums)
        # print(sums)
        # print()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s = nums[i]+nums[j]
                #print('i: {}, j:{}, s:{}, target-s:{}'.format(i, j, s, target-s))
                if target-s in sums:
                    pairs = sums[target-s]
                    for pair in pairs:
                        if pair[0]!=i and pair[0]!=j and pair[1]!=i and pair[1]!=j:
                            four_sum = sorted([nums[i], nums[j], nums[pair[0]], nums[pair[1]]])
                            # print('fourSum:', four_sum)
                            # print()
                            if four_sum not in soln:
                                soln.append(four_sum)
            #print()
        #print(soln)
        return soln