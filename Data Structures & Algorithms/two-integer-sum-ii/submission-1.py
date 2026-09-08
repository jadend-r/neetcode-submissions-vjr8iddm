class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two ptrs l, r
            #if arr[l] + arr[r] == target, return indicies
            # > target, shift right -> left
            # < target, shift left -> right

        l, r = 0, len(numbers) - 1
        while l < r:
            ts = numbers[l] + numbers[r]
            if ts == target:
                return [l + 1, r + 1]
            elif ts > target:
                r -= 1
            else:
                l += 1