from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        shortest = strs[0]
        for string in strs:
            if len(string) < len(shortest):
                shortest = string
        
        if not shortest:
            return ""

        prefix = ""
        i = 0
        while i < len(shortest):
            current = strs[0][i]
            for string in strs:
                if string[i] != current:
                    return prefix
            prefix += current
            i += 1
        
        return prefix

if __name__ == "__main__":
    strs = ["","b"]
    A = Solution()
    print(A.longestCommonPrefix(strs))
