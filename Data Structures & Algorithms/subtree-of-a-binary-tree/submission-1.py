# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # do dfs on root until a node matches with subroot's node
        # once met, call a isSameTree function - that has base cases (if only one node is there or vals are unequal, return false on line 2. line 1, return true if the two nodes are none. iteration step: return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)). if result is true, then the problem is true.
        if not root:
            return False
        elif root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))