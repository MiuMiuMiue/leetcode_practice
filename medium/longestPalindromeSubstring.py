class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0

        check = [[False for _ in range(len(s))] for _ in range(len(s))]

        for j in range(len(s)):
            check[j][j] = True
            for i in range(j):
                if s[i] == s[j] and (j - i <= 2 or check[i+1][j-1]):
                    check[i][j] = True
                    if j - i + 1 > r - l + 1:
                        l, r = i, j

        return s[l:r+1]

if __name__ == "__main__":
    A = Solution()
    print(A.longestPalindrome("babad"))