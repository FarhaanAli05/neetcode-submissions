# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int

        logic: at each node, calculate the maximum total of its left subtree plus the maximum total of its right subtree. add them up to the root and calculate the running maximum of all those left right subtree max sums. return that running maximum

        tc: o(n)
        sc: o(h)
        """
        running_max_sum = [root.val]
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            running_max_sum[0] = max(running_max_sum[0], left + right + node.val, left + node.val, right + node.val, node.val)
            return max(max(left, right) + node.val, node.val)
        dfs(root)
        return running_max_sum[0]