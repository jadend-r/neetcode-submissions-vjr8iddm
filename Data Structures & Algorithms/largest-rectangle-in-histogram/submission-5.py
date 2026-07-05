class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         #monotonic increasing stack 
            #pop all taller bars and compute their area
            #push each bar onto the stack
        #O(n) time #O(n) space
        heights.append(0) # trick so all remaining heights are flushed at the end
        #(height, startIdx)
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, start = stack.pop()
                maxArea = max(maxArea, height * (i - start))
            stack.append((h, start))

        # for bars that extend all the way to the end
        # append height 0 avoids this
        # while stack:
        #     height, start = stack.pop()
        #     maxArea = max(maxArea, height * (len(heights) - start))

        return maxArea

        #[2,1,5,6,2,3] [(1, 0), (2, 1), (3, 5)]