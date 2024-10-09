from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = -1

        while i < j:
            maxArea = max(min(height[i], height[j]) * (j - i), maxArea)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea