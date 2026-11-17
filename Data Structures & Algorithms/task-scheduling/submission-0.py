from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        logic: get frequencies of tasks.
        add those frequencies to a max heap
        the most frequent frequency, add 1 to that and add it to a queue. the queue will store the frequency + 1 and time + n (basically when to dequeue)
        while the hash map or the queue exist, run a while loop with the above operation. if the front of the queue's time has come, pop it and add it to the max heap. if there is a max heap, pop the top element and add it to the queue.

        tc: o(t+i)
        sc: o(1), because freqs, q, and m_heap hold at most constant 26 letters
        """
        freqs = Counter(tasks)
        m_heap = []
        for freq in freqs.values():
            heapq.heappush(m_heap, -freq)
        heapq.heapify(m_heap)
        q = deque()
        time = 0
        while m_heap or q:
            time += 1
            if m_heap:
                most_freq = heapq.heappop(m_heap) + 1
                if most_freq:
                    q.append([most_freq,time+n])
            if q and q[0][1] == time:
                heapq.heappush(m_heap, q.popleft()[0])
        return time