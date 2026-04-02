class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify_max(maxHeap)

        for i in range(k - 1):
            heapq.heappop_max(maxHeap)

        return maxHeap[0]