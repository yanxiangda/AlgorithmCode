
# 二叉树的最大深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.maxDeep(root)
    """
    返回以node为根的子树的最大深度
    """
    def maxDeep(self, node):
        if node.left != None:
            leftMax = self.maxDeep(node.left)
        else:
            leftMax = 0
        if node.right != None:
            rightMax = self.maxDeep(node.right)
        else:
            rightMax = 0
        return (leftMax + 1) if leftMax > rightMax else (rightMax + 1)





