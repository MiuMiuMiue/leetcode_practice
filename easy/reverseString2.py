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

def test_1(Ans):
    s = ""
    k = 2
    print(Ans.reverseStr(s, k) == "")

def test_2(Ans):
    s = "a"
    k = 3
    print(Ans.reverseStr(s, k) == "a")

def test_3(Ans):
    s = "abandon"
    k = 5
    print(Ans.reverseStr(s, k) == "dnabaon")

def test_4(Ans):
    s = "abandon"
    k = 7
    print(Ans.reverseStr(s, k) == "nodnaba")

if __name__ == "__main__":
    A = Solution()
    
    test_1(A)
    test_2(A)
    test_3(A)
    test_4(A)

