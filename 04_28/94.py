# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        helper(root,res)
        return res
        
def helper(root, res):
    if root != None:
        if root.left != None:
            helper(root.left,res)
        res.append(root.val)
        if root.right != None:
            helper(root.right,res)
            