class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip()
        i = len(s) - 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length