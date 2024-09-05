from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxContainer = 0

        while l < r:
            maxContainer = max(min(height[l], height[r]) * (r - l), maxContainer)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxContainer