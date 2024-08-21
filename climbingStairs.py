class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp_array = [0] * n
        dp_array[0], dp_array[1] = 1, 2

        for n in range(2, n):
            dp_array[n] += dp_array[n-1] + dp_array[n - 2]

        return dp_array[-1]