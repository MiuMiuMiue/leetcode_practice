from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            second_target = target - nums[i]
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                third_target = second_target - nums[j]
                seen = set()
                k = j + 1
                while k < len(nums):
                    if third_target - nums[k] in seen:
                        results.append([nums[i], nums[j], nums[k], third_target - nums[k]])
                        while k < len(nums) - 1 and nums[k] == nums[k + 1]:
                            k += 1
                    else:
                        seen.add(nums[k])
                    k += 1
        return results