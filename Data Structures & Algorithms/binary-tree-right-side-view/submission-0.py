# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        logic: do a bfs and the last node you process per a level, add that to a list and return the list at the end. how: the queue stores tuples. the first index is the node itself, the second is the level it's on. node.left and node.right should be the current level + 1. as soon as you pop a node, check if its next node's second index matches the current node's level (check the top of the queue, o(1)). if it doesn't, that value must be added to the result list.

        tc: o(n)
        sc: o(n)
        """
        if not root:
            return []
        res = []
        queue = deque([(root,1)])
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
            if not queue or level != queue[0][1]:
                res.append(node.val)
        return res