class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = { i: [] for i in range(n) }
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        seen = {0}
        def dfs(node, parent):
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n