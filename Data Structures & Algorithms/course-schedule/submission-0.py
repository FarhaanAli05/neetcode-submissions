class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = { i: [] for i in range(numCourses) }
        for prequisite in prerequisites:
            adj_list[prequisite[0]].append(prequisite[1])
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        def dfs(node):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True
            states[node] = VISITING
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True