from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                nums.pop(i + 1)
            
            i += 1
        

        return i

if __name__ == "__main__":
    nums = [1, 1]
    A = Solution()
    print(A.removeDuplicates(nums))
    print(nums)