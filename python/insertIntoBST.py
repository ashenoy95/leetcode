# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST_recursive(self, root: TreeNode, val: int) -> TreeNode:   
        """
        Recursive
        """
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
        
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:  
        """
        Iterative
        """
        if not root:
            return TreeNode(val)
        
        node = root
        parent = root
        
        while node:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
                
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
            
        return root
    
