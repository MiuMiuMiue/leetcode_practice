from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_dict = dict(Counter(t))
        
        i = 0
        length = 10 ** 5 + 1
        answer = ""
        s_dict = defaultdict(int)

        for j in range(len(s)):
            if s[j] in t_dict:
                s_dict[s[j]] += 1
            
            substring = True
            for char in t_dict:
                if s_dict[char] < t_dict[char]:
                    substring = False

            if substring:
                while s[i] not in t_dict or s_dict[s[i]] > t_dict[s[i]]:
                    s_dict[s[i]] -= 1
                    i += 1
                if j - i + 1 < length:
                    length = j - i + 1
                    answer = s[i:j + 1]
        
        return answer
            