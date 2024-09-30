from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # check = {}
        # for num in nums:
        #     if num not in check:
        #         check[num] = 1
        #     else:
        #         check[num] += 1
        
        # for num in check:
        #     if check[num] > len(nums) // 2:
        #         return num
        
        nums.sort()
        return nums[len(nums) // 2]