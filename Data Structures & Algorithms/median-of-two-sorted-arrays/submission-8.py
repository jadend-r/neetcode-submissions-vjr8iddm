class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #set num1 to be the shorter array
        #always binafry search on our smaller array

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        #binary search over nums1
        l, r = 0, len(nums1)
        while l <= r:
            i = (r + l) // 2
            j = half - i

            L1 = nums1[i-1] if i > 0 else -math.inf
            L2 = nums2[j-1] if j > 0 else -math.inf
            R1 = nums1[i] if i < len(nums1) else math.inf
            R2 = nums2[j] if j < len(nums2) else math.inf

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                   
                else:
                    return max(L1, L2)
            elif L1 > R2:
                r = i - 1
            else:
                l = i + 1
