class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]

        logic: calculate the distance between each point and 0,0. based on that, we can min heapify that and discard len(points)-k points in that heap. return that heap.

        add each result of points distance from origin to a distances array. before that, map the result to the point you're on. heapify the distances array. discard len(points)-k distances. finally, for each distance, add its corresponding point to a result array.

        tc: o(n log n)
        sc: o(n)
        """
        distances = []
        res = []
        for point in points:
            x_dist = point[0] - 0
            y_dist = point[1] - 0
            distance = x_dist**2 + y_dist**2
            distances.append((distance,point))
        heapq.heapify(distances)
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res