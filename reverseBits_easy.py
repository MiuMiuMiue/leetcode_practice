class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            current = 0x1 & n
            result = result << 1 | current
            n = n >> 1
        
        return result