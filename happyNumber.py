class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()

        while n != 1:
            if n in check:
                return False
            check.add(n)
            
            current_sum = 0
            start = 10
            while n > 0:
                left_most = n % start
                current_sum += left_most ** 2
                n = n // 10
            
            n = current_sum
        
        return True