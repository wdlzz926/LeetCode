# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder [root, leftchildren, rightchilden]
        # inorder [leftchildren,root,rightchidren]  
        if inorder == []:
            return None
        rootVal = preorder.pop(0)
        index = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder,inorder[0:index])
        root.right = self.buildTree(preorder,inorder[index+1:])
        return root