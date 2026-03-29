class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}
       
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, count in counts.items():
            freq[count].append(n)

        res = []
        for _, ns in enumerate(freq[::-1]):
            for n in ns:
                res.append(n)
                if len(res) == k:
                    return res