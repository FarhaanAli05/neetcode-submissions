class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        parents = [i for i in range(n)] # SC: O(V)
        ranked = [1] * n # SC: O(V)

        def find(n1): # TC: O(V)
            res = n1
            while parents[res] != res:
                parents[res] = parents[parents[res]] # points you directly to the grandparent node
                res = parents[res]
            return res
        
        def union(n1, n2): # TC: O(V)
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if ranked[p1] >= ranked[p2]:
                ranked[p1] += ranked[p2]
                parents[p2] = p1
            else:
                ranked[p2] += ranked[p1]
                parents[p1] = p2
            return 1

        for a, b in edges: # TC: O(E)
            components -= union(a, b)
        
        return components

        # Overall TC: O(V+E), SC: O(V)

"""
        # logic: define parent array and ranked array
        # parent array keeps track of each node's parent, ranked keeps track of the size of each union
        # find function finds a node's parent node
        # union function combines two nodes, updates the parent's ranked by 1 (increment), and makes the child's parent the parent
        # each successful union returns a 1 which decrements the components
"""