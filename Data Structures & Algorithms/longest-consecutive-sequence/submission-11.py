class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force: sort array then simply count increasing sequences, n log n
        #optimize to o(n): turn nums into set, for each num check left nei
            #if no left nei -> start new sequence
            #O(n) time/space
        
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                leng = 0
                while num + leng in nums_set:
                    leng += 1
                longest = max(longest, leng)
                    

        return longest
