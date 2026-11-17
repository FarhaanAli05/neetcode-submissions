class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = { i: [] for i in range(n) }
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        components = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei)
        
        seen = set()

        for i in range(n):
            if i not in seen:
                dfs(i)
                components += 1

        return components