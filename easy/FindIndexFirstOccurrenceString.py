class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            current = i
            same = True
            for char in needle:
                if char != haystack[current]:
                    same = False
                    break
                current += 1
            if same:
                return i
        return -1