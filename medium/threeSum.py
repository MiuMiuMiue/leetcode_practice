from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            seen = set()
            j = i + 1
            while j < len(nums):
                if 0 - nums[i] - nums[j] in seen:
                    results.append([nums[i], nums[j], 0 - nums[i] - nums[j]])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return results