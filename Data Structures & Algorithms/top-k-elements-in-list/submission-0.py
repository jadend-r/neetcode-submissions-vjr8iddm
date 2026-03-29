class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]
        output = []
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, count in counts.items():
            freq[count].append(n)
            
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output

        return output

        