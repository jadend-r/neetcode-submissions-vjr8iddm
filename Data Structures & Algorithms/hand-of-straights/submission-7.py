class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # time O(n log n)
        if len(hand) % groupSize != 0:
            return False

        count = {}
        # count each card that we have O(n)
        for c in hand:
            count[c] = 1 + count.get(c, 0)
        # minHeap to give us the smallest card in hand
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        # try to form the group of size k starting from the smallest
        while minHeap:
            smallest = minHeap[0]

            for c in range(smallest, smallest + groupSize):
                if c not in count:
                    return False
                count[c] -= 1
                if count[c] == 0:
                    if c != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True