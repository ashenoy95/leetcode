# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        inorder = []
        curr = root
        
        while curr:
            stack.append(curr)
            curr = curr.left
        
        while stack:
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
            
            while curr:
                stack.append(curr)
                curr = curr.left
            
        return inorder
            