

# 最大二叉树
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(sys.maxsize)
        currentNode = root
        for i in nums:
            newNode = Treenode(i)
            if i < currentNode.val:
                currentNode.right = newNode
            else:

    def OptimizationNode(self, currentNode, nums, index):
        val = nums[index]
        newNode = Treenode(val)
        if val < currentNode.val:
            nextNode = self.OptimizationNode(self, currentNode, nums, index + 1)
            if nextNode.val > newNode.val:
                nextNode.left = newNode
                currentNode.right = nextNode
            else:
                currentNode.right = newNode
        else:







