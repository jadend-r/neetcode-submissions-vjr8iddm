class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        minn = math.inf

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] >= nums[l]:
                minn = min(minn, nums[l])
                l = m + 1
            else:
                minn = min(minn, nums[m])
                r = m - 1

        return minn