class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            columnNumber = columnNumber // 26
            res += chr(ord("A")+r)
        return res[::-1]

if __name__ == "__main__":
    A = Solution()
    print(A.convertToTitle(701))