# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int

        do a dfs on the tree.
        for each depth first search "plunge", keep track of the running maximum value in that path. if the current node is LESS than the running maximum, DON'T count it. if it's at LEAST the current running maximum, that's a good node and the result must be incremented.

        tc: o(n)
        sc: o(h), h is the height of the tree
        """
        good_nodes = [0]
        running_max = root.val
        def dfs(node, running_max):
            if not node:
                return
            if node.val >= running_max:
                good_nodes[0] += 1
            running_max = max(running_max, node.val)
            dfs(node.left, running_max)
            dfs(node.right, running_max)
        dfs(root, running_max)
        return good_nodes[0]