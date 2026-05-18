class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # easy brute force solution O(m + n) time O(m + n) space
            # 1. combine num1 + num2 into 1 single list (merge two sorted lists)
            # 2. compute the midpoint/median 

        i, j = 0, 0
        combined = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            combined += nums1[i:]
        elif j < len(nums2):
            combined += nums2[j:]

        print(combined)
        #compute median
        if len(combined) % 2 == 0:
            print("even")
            return (combined[len(combined) // 2] + combined[len(combined) // 2 - 1]) / 2
        else:
            print("huh")
            return combined[len(combined) // 2] 
        