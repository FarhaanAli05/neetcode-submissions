class KthLargest:

    # logic: heapify nums, heappop from nums until it is size k
    # for add, heappush to nums, if its length exceeds k, heappop. finally return the root

    # tc: o(n log n) for init, o(log n) for add
    # sc: o(1)
    
    # test case
    # ["KthLargest", "add", "add", "add", "add", "add"]
    # [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

    # k = 3
    # [4, 5, 8, 2]
    # self.nums = [4, 5, 8]
    # --- add 3
    # [4, 5, 8], res = 4
    # --- add 5
    # [5, 8, 5], res = 5
    # --- add 10
    # [5, 8, 10], res = 5
    # --- add 9
    # [8, 10, 9], res = 8
    # --- add 4
    # [8, 10, 9], res = 8

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)