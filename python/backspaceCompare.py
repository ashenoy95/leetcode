class Solution:    
    def _parse(self, s: str, idx: int, skip_ctr: int):
        """
        Helper function to parse str in reverse till '#' is encountered
        Keep count of how many '#'s & skip those many chars
        """
        while idx >= 0:
            if s[idx] == '#':
                skip_ctr += 1
                idx -= 1
            elif skip_ctr:
                skip_ctr -= 1
                idx -= 1
            else:
                break
        
        return idx, skip_ctr
    
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Stack would use O(n) space
        2 ptrs brings down to O(1) space
        """
        i = len(S) - 1
        j = len(T) - 1
        s_skip = 0
        t_skip = 0
        
        while (i >= 0) or (j >= 0):
            # parse S & T till non-backspace char & then compare
            i, s_skip = self._parse(S, i, s_skip)
            j, t_skip = self._parse(T, j, t_skip)
            
            # break if 
            # 1. char mismatch
            # 2. at any one of the strings is shorter than the other
            if ((i >= 0) and (j >= 0) and (S[i] != T[j])) or ((i >= 0) != (j >= 0)):
                return False
            
            i -= 1
            j -= 1

        return True
    
