"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        seen = set()
        seen.add(node)
        stack = [node]
        o_to_n = {}

        def dfs(node):
            while stack:
                popped = stack.pop()
                o_to_n[popped] = Node(val = popped.val)
                for nei_node in popped.neighbors:
                    if nei_node not in seen:
                        seen.add(nei_node)
                        stack.append(nei_node)
            
            for old_node, new_nodes in o_to_n.items():
                for nei in old_node.neighbors:
                    o_to_n[old_node].neighbors.append(o_to_n[nei])

        dfs(node)
        return o_to_n[node]