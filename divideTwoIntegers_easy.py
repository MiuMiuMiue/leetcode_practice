class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) == 1:
            return dividend

        neg = False
        if dividend < 0 and divisor > 0:
            neg = True
        elif divisor < 0 and dividend > 0:
            neg = True
        
        dividend, divisor = abs(dividend), abs(divisor)

        i = 0
        current = 0

        while current < dividend:
            current += divisor
            i += 1
        
        if current > dividend:
            return max(0, i - 1) if not neg else - max(0, i - 1)
        return i if not neg else -i

if __name__ == "__main__":
    A = Solution()
    print(A.divide(10, 3))