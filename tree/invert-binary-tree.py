
# 翻转二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inverse(root)
        return root
        
    def inverse(self, node):
        # 如果翻转到node=None, 停止
        if node == None:
            return
        ass = node.left
        node.left = node.right
        node.right = ass
        self.inverse(node.left)
        self.inverse(node.right)


