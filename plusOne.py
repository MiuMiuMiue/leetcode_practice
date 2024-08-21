from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = False

        digits[-1] += 1
        if digits[-1] == 10:
            one = True
            digits[-1] = 0
        else:
            return digits
        
        i = len(digits) - 2
        while one and i >= 0:
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                one = True
            else:
                one = False
            i -= 1
        
        if one:
            return [1] + digits
        return digits
            