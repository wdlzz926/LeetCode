# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if node:
                inorder(node.left)
                self.ans = min(self.ans, node.val-self.prev)
                self.prev = node.val
                inorder(node.right)
        self.prev = float('-inf')
        self.ans = float('inf')
        inorder(root)
        return self.ans