class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = { i: [] for i in range(n) }
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        # {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
        # n = 5

        master = set()

        def dfs(node):
            # seen = {3, 4}
            # node = 3
            if node in seen:
                return
            seen.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        for i in range(n):
            seen = set()
            dfs(i)
            master.add(tuple(seen))
        
        # master = {({0, 1, 2}), ({3, 4})}

        return len(master)