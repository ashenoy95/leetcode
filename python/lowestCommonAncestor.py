# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            print('\ncurr node:', root.val if root else root)
        if not root or p.val==root.val or q.val==root.val:
            print('node is null or node = p or q so returning')
            return root
        print('curr node:', root.val if root else root)
        print('calling left')
        left = self.lowestCommonAncestor(root.left, p, q)
        print('curr node:', root.val if root else root)
        print('left:', left.val if left else left)
        print('calling right')
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            print('left: {}, right: {}'.format(left.val, right.val))
            print('both left and right exist so returning\n', root.val)
            return root
        
        if left:
            print('left exists so returning i.e. second node is not in right subtree\n', left.val)
            return left
        if right:
            print('right exists so returning\n', right.val)
            return right
        print('left and right are both null\n')
        return 