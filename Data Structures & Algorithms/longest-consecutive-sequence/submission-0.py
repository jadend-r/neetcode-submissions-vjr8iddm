class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in nums: #no left neighbor means start of sequence
                length = 0
                while num + length in nums: #count each consecutive starting at the start of sequence
                    length += 1
                longest = max(length, longest)

        return longest