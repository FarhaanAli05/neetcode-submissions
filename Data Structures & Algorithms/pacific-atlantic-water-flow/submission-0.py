class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # logic: add pacific ocean's border nodes to a pacific seen set and queue
        # add atlantic ocean's border nodes to an atlantic seen set and queue
        # the set and queue are passed into a bfs function
        # the multiple starting coordinates in the queues make this a multi-source bfs graph traversal problem
        # since the border nodes reach each ocean, each node that passes the bfs iteration criteria is a node that reaches the ocean too
        # at the end, intersect the seen sets for pacific and atlantic oceans
        # criteria: a node must be at least the previous node for the bfs to traverse
        m, n = len(heights), len(heights[0])
        seen_pacific = set()
        q_pacific = deque()
        seen_atlantic = set()
        q_atlantic = deque()

        # add pacific border coordinates
        for i in range(n):
            seen_pacific.add((0, i))
            q_pacific.append((0, i))
        for i in range(1, m):
            seen_pacific.add((i, 0))
            q_pacific.append((i, 0))
        # add atlantic border coordinates
        for i in range(n):
            seen_atlantic.add((m-1, i))
            q_atlantic.append((m-1, i))
        for i in range(m - 1):
            seen_atlantic.add((i, n-1))
            q_atlantic.append((i, n-1))
        
        def bfs(seen, q):
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        q.append((nr, nc))
        
        bfs(seen_pacific, q_pacific)
        bfs(seen_atlantic, q_atlantic)
        return list(seen_pacific.intersection(seen_atlantic))