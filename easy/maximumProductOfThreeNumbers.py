from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxNums = [-1001, -1001, -1001]
        minNums = [1001, 1001, 1001]

        seenMax = set()
        seenMin = set()
        maxIndex = 0
        minIndex = 0

        for i in range(3):
            for j in range(len(nums)):
                if j not in seenMax and nums[j] > maxNums[i]:
                    maxNums[i] = nums[j]
                    maxIndex = j

                if j not in seenMin and nums[j] < minNums[i]:
                    minNums[i] = nums[j]
                    minIndex = j
            
            seenMax.add(maxIndex)
            seenMin.add(minIndex)
        
        prod1 = maxNums[0] * maxNums[1] * maxNums[2]
        prod2 = minNums[0] * minNums[1] * maxNums[0]
        
        return prod1 if prod1 > prod2 else prod2

