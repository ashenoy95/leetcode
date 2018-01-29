class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in groups:
                groups[sorted_s] = [s]
            else:
                groups[sorted_s].append(s)
        return groups.values()