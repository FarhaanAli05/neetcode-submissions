# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        do a bfs of the binary tree and all nodes and null nodes to a stringified list

        tc: o(n)
        sc: o(n)
        """
        if not root:
            return ""
        nodes = [str(root.val)]
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            nodes.append(str(node.left.val) if node.left else str(None))
            if node.right:
                q.append(node.right)
            nodes.append(str(node.right.val) if node.right else str(None))
        return ",".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        take this string, convert it to a list. take the root node, add it to a treenode and a queue. pop from the queue and add the next two nodes in the list, assign them as the root's left and right child. if they're non-null, add them to a queue one at a time. repeat the algorithm while the queue has values. use a pointer that iterates through the list gradually.

        tc: o(n)
        sc: o(n)
        """
        if data == "":
            return
        nodes = data.split(",")
        for i in range(len(nodes)):
            if nodes[i] != "None":
                nodes[i] = int(nodes[i])
            else:
                nodes[i] = None
        root = TreeNode(nodes[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] is not None:
                left_node = TreeNode(nodes[i])
                node.left = left_node
                q.append(left_node)
            i += 1
            if nodes[i] is not None:
                right_node = TreeNode(nodes[i])
                node.right = right_node
                q.append(right_node)
            i += 1
        return root