from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        left_max, right_max = [0] * len(height), [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        for i in range(len(height) - 1):
            total_water += max(0, min(left_max[i], right_max[i]) - height[i])

        return total_water
