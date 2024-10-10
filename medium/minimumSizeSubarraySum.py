from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        current_sum = 0
        length = 10 ** 5 + 1

        for j in range(len(nums)):
            current_sum += nums[j]

            while current_sum >= target:
                length = min(length, j - i + 1)
                current_sum -= nums[i]
                i += 1
        
        return length if length < 10 ** 5 + 1 else 0