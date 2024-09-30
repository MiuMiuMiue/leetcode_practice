class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for length in range(len(nums) - 1, 0, -1):
            for i in range(length):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        
        return nums[0]