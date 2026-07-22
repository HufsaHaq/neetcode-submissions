class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2 pointer algorithm
        start = 0
        end = len(heights) - 1
        max_height = 0
        while start < end:
            height = (end-start) * min(heights[start], heights[end])
            if heights[start] < heights[end]:
                start += 1
            else:
                end -=1
            max_height = max(max_height, height)
        return max_height
