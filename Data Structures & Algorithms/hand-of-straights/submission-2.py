class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
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
        print("minH", minHeap)
        while minHeap:
            smallest = minHeap[0]

            for c in range(smallest, smallest + groupSize):
                if c not in count or count[c] == 0:
                    return False
                print("count", c, "before", count[c])
                count[c] -= 1
                print("count", c, "after", count[c])
                if count[c] == 0:
                    if c != minHeap[0]:
                        print("ret 2", c, minHeap)
                        return False
                    print("popping", minHeap[0], "before", minHeap)
                    heapq.heappop(minHeap)
                    print("minHeap after pop", minHeap)
        return True