class Solution(object):
    def generate(self, s, left, right, n, combinations):
        if left==n and right==n:
            combinations.append(s)
        else:
            if left<n:
                self.generate(s+'(', left+1, right, n, combinations)
            if right<left:
                self.generate(s+')', left, right+1, n, combinations)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = []
        self.generate('',0,0,n, combinations)
        return combinations