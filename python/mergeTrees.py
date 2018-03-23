 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

 class Solution(object):
 	def mergeTrees(self, t1, t2):
 		q = []



while t1.left or t1.right or t2.left or t2.right:
            t3.val = t1.val + t2.val
            if t1.left and t2.left:
                t3.left = t1.left.val + t2.left.val
            if t1.right and t2.right:
                t3.right = t1.right.val + t2.right.val
            if t1.left and not t2.left:
                t3.left = t1.left
            else:
                t3.left = t2.left
            if t1.right and not t2.right:
                t3.right = t2.right