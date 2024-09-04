class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x = abs(x)

        result = 0

        while x:
            current = x % 10
            x //= 10
            result += current
            result *= 10
        
        result = result * neg // 10
        return result if result >= - 2 ** 31 and result <= 2 ** 31 - 1 else 0