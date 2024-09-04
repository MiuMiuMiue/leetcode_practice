class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        length = 0
        l = 0

        for r in range(len(s)):
            current = s[r]
            if current in check and check[current] >= l:
                l = check[current] + 1
            else:
                length = max(length, r - l + 1)
            check[current] = r
        
        return length