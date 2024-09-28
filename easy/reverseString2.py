class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        
        result = ""
        i = 0
        while i < len(s):
            if i % (2 * k) == 0 and i + k < len(s):
                for j in range(k - 1, -1, -1):
                    result += s[i + j]
                i += k
            elif i % (2 * k) == 0:
                for j in range(len(s) - i - 1, -1, -1):
                    result += s[i + j]
                return result
            else:
                result += s[i:i+k]
                i += k
        
        return result


if __name__ == "__main__":
    A = Solution()
    print(A.reverseStr("abcdefg", 3))
