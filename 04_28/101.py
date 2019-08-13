# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(l_n,r_n):
            if l_n == None and r_n == None: return True
            if l_n == None or r_n == None: return False
            return (l_n.val == r_n.val) and isMirror(l_n.left,r_n.right) and isMirror(l_n.right,r_n.left)
        if root is None:
            return True
        return isMirror(root.left,root.right)