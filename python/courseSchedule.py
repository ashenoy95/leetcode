# detecting cycle in directed graph 

# using dfs
class Solution:
    def dfs(self, course, graph, visited):
        if visited[course]==-1:
            return False
        
        visited[course] = -1
        
        for succ in graph[course]:
            if visited[succ]==1:
                continue
            if not self.dfs(succ, graph, visited):
                return False
        
        visited[course] = 1
        
        return True
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {course: [] for course in range(numCourses)}
        visited = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        for course in range(numCourses):
            if not self.dfs(course, graph, visited):
                return False
            
        return True
                

# using coloring
"""
class Solution(object):
    def dfs(self, course, prerequisites, white, gray, black):
        gray.add(course)
        neighbors = [prereq[1] for prereq in prerequisites if prereq[0]==course]
        for c in neighbors:
            if c not in black:
                if c in gray:
                    return False
                if not self.dfs(c, prerequisites, white, gray, black):
                    return False
        gray.remove(course)
        black.add(course)
        return True
    
    def canFinish(self, numCourses, prerequisites):
        white = {course for course in range(numCourses)}
        gray = set()
        black = set()  
        while white:
            if not self.dfs(white.pop(), prerequisites, white, gray, black):
                return False
        return True
"""    