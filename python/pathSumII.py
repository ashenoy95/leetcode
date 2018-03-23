#Beats 98% of solutions

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, sum, res, path):
        if not node:
            return 
        path.append(node.val)
        if not node.left and not node.right and sum==node.val:
            res.append([val for val in path])
            return
        if node.left:
            self.dfs(node.left, sum-node.val, res, path)
            path.pop()
        if node.right:
            self.dfs(node.right, sum-node.val, res, path)
            path.pop()
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, sum, res, [])
        return res
        