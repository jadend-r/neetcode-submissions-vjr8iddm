class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i, num in enumerate(nums):
            if num - 1 not in nums:
                count = 0
                j = 0
                while num + j in nums:
                    count += 1
                    j += 1
                    longest = max(longest, count)

        return longest