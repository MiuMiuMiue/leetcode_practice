from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last = [1]

        for level in range(1, rowIndex + 1):
            dummy = [0] + last + [0]
            current = []
            for i in range(1, len(dummy)):
                current.append(dummy[i - 1] + dummy[i])
            last = current
        
        return last
