class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keypad = {
            '0': ' ',
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        temp = []
        temp2 = []
        result = []
        for d in digits:
            temp = [c for c in keypad[d]]
            if not result:
                result = [c for c in keypad[d]]
                continue
            for r in result:
                for t in temp:
                    temp2.append(r+t)
            result = temp2
            temp2 = []
        return result
        