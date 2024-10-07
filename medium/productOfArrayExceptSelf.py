from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [1] * len(nums)
        rightToLeft = [1] * len(nums)
        answer = [0] * len(nums)

        for i in range(1, len(nums)):
            leftToRight[i] = leftToRight[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightToLeft[i] = rightToLeft[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answer[i] = leftToRight[i] * rightToLeft[i]

        return answer
