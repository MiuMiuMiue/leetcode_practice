class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        j = x

        while i <= j:
            mid = (i + j) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                i = mid + 1
            else:
                j = mid - 1
        
        return i