from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [-1] * len(nums)
        jumps[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            minCount = 9999
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and jumps[i + j] >= 0:
                    minCount = min(minCount, jumps[i + j] + 1)
            jumps[i] = minCount

        return jumps[0]

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    A = Solution()
    print(A.jump(nums))
