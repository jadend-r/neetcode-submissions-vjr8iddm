class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #init O(nlogn) time O(n) space
       self.minHeap = nums
       self.k = k
       heapq.heapify(self.minHeap)
       #O(nlogn)
       while len(self.minHeap) > k: #O(n)
            heapq.heappop(self.minHeap) #O(logn)

    def add(self, val: int) -> int:
        #overall O(logk) time O(k) space
        heapq.heappush(self.minHeap, val) #O(logn)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #O(logn)
        return self.minHeap[0]
