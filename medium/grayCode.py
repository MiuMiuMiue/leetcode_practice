from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        seen = set()
        result = []
        seen.add(0)
        result.append(0)
        last = 0

        while len(seen) < 2 ** n:
            for i in range(n):
                mask = 1 << i
                if last ^ mask not in seen:
                    seen.add(last ^ mask)
                    result.append(last ^ mask)
                    last = last ^ mask
                    break
        
        return result