class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ''
        if numRows==1 or len(s)<numRows:
            return s

        zigzag_list = ['' for row in range(numRows)]
        row = 0
        flag = True
        zigzag = ''
        
        for char in s:
            zigzag_list[row] += char
            if flag:
                row += 1
            else:
                row -= 1
            if row==numRows:
                flag = False
                row = numRows-2
            if row==-1:
                flag = True
                row = 1
                
        for row in zigzag_list:
            zigzag += row
        
        return zigzag