class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for char in t:
            if j == len(s):
                return True
            if char == s[j]:
                j += 1
        
        return j == len(s)