class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            print(columnNumber)
            r = (columnNumber-1) % 26
            columnNumber = (columnNumber-1)// 26
            print(r, columnNumber, ord("A") + r)
            res += chr(ord("A")+r)
        return res[::-1]

if __name__ == "__main__":
    A = Solution()
    print(A.convertToTitle(701))