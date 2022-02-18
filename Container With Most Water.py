class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_vol = 0
        while start < end:
            max_vol = max(max_vol, (end-start)*min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_vol