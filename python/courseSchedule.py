# detecting cycle in directed graph 

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
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        white = {course for course in range(numCourses)}
        gray = set()
        black = set()  
        while white:
            if not self.dfs(white.pop(), prerequisites, white, gray, black):
                return False
        return True
    