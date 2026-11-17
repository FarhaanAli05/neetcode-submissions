class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = { i: [] for i in range(n) }
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        master = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        for i in range(n):
            seen = set()
            dfs(i)
            master.add(frozenset(seen))

        return len(master)