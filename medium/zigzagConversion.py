class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        
        row = 0
        sign = 1

        for i in range(len(s)):
            zigzag[row].append(s[i])

            if row + sign == 0 or row + sign == numRows - 1:
                row += sign
                sign *= -1
            else:
                row += sign
        
        result = ""
        for row in zigzag:
            result += "".join(row)
        
        return result