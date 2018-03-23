#Treating as a search problem and using A* search algorithm

import Queue as Q

class Solution(object):
    def dist(self, start, end):
        moves = 0
        for i in range(len(start)):
            if start[i]!=end[i]:
                moves += 1
        return moves
    
    
    def succFunc(self, gene, bank_dict):
        valid_mutations = set()
        choices = ['A', 'C', 'G', 'T']
        
        for choice in choices:
            for i in range(len(gene)):
                if gene[i]!=choice:
                    temp = gene[:i] + choice + gene[i+1:]
                    if ''.join(temp) in bank_dict:
                        valid_mutations.add(temp)                    
        return valid_mutations
    
    
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        moves = 0
        bank_dict = {gene:None for gene in bank}

        fringe = Q.PriorityQueue()
        visited = {gene:False for gene in bank}
        f = {gene:0 for gene in bank}
        succ = {}

        if end==start:
            return 0

        fringe.put((0, start))
        visited[start] = True
        
        while True:
            if fringe.empty():
                return -1

            gene = fringe.get()[1]
            moves += 1
                
            if gene==end:
                return moves-1
            
            succ[gene] = self.succFunc(gene, bank_dict)

            for mutation in succ[gene]:
                if visited[mutation]:
                    continue
                f[mutation] = 1 + self.dist(mutation, end)
                fringe.put((f[mutation], mutation))
                visited[mutation] = True
                
                        