class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p,q = 0, len(heights) - 1
        max_area = 0
        while p < q:
            current_area = (q - p) * min(heights[p], heights[q])
            max_area = max(current_area, max_area)
            if heights[p] > heights[q]:
                q -= 1
            else:
                p += 1
        return max_area