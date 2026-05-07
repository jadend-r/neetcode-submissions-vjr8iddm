class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for card in hand:
            count[card] = 1 + count.get(card, 0)

        minHeap = [k for k in count.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False #popping anything other than min value creates a hole for later groups
                    heapq.heappop(minHeap)

        return True