class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in seen:
                length = max(length, j - i + 1)
                seen.add(s[j])
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
                seen.add(s[j])
        return length