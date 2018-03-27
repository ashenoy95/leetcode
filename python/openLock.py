import queue as Q

class Solution:
    def dist(self, start, end):
        turns = 0
        for i in range(4):
            d = abs(int(start[i])-int(end[i]))
            if d>4:
                d = 9-d
            turns += d
        return turns
    
    
    def succFunc(self, seq, deadends_dict):
        valid_moves = set()
        
        for i in range(4):
            wheel = int(seq[i])
            move1 = seq[:i] + str(wheel+1) + seq[i+1:]
            move2 = seq[:i] + str(wheel-1) + seq[i+1:]
            
            if wheel==0:
                move2 = seq[:i] + '9' + seq[i+1:]
            elif wheel==9:
                move1 = seq[:i] + '0' + seq[i+1:]
            
            if move1 not in deadends_dict:
                valid_moves.add(move1)
            if move2 not in deadends_dict:
                valid_moves.add(move2)
                
        return valid_moves
    
    
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        start = '0000'
        fringe = Q.PriorityQueue()
        visited = {}
        turns = -1
        deadends_dict = {deadend:None for deadend in deadends}
        
        if start in deadends_dict:
            return -1
        
        if target==start:
            return 0
        
        fringe.put((0, start, turns))
        
        while True:
            if fringe.empty():
                return -1
            tup = fringe.get()
            seq = tup[1]
            if seq in visited:
                continue
            else:
                visited[seq] = True
            turns = tup[2] + 1
            
            if seq==target:
                return turns
            
            succ = self.succFunc(seq, deadends_dict)
            
            for s in succ:
                if s not in visited:
                    f = turns + self.dist(s, target)
                    fringe.put((f, s, turns))