class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elems = {}
        for num in nums:
            if num not in elems:
                elems[num] = 1
            else:
                elems[num] += 1
        elems = sorted(elems, key=lambda num: elems[num], reverse=True)
        return elems[:k]
        
        