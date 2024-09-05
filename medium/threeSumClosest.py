from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 2 ** 31 - 1

        for i in range(len(nums)):
            current_target = target - nums[i]
            current_best = 2 ** 31 - 1
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if abs(current_target - nums[j] - nums[k]) < abs(current_best - current_target):
                    current_best = nums[j] + nums[k]
                
                if nums[j] + nums[k] > current_target:
                    k -= 1
                elif nums[j] + nums[k] < current_target:
                    j += 1
                else:
                    break

            if abs(target - result) > abs(target - nums[i] - current_best):
                result = nums[i] + current_best
        
        return result

if __name__ == "__main__":
    nums = [4,0,5,-5,3,3,0,-4,-5]
    A = Solution()
    print(A.threeSumClosest(nums, -2))