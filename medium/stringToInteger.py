class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        time = 1 if s[0] != "-" else -1
        if s[0] == "+" or s[0] == "-":
            s = s[1:]

        start = False
        result = 0

        for i in range(len(s)):
            if not start and ord(s[i]) in range(48, 58):
                start = True
            elif ord(s[i]) not in range(48, 58):
                if result * time < -2**31:
                    return -2**31
                elif result * time > 2**31-1:
                    return 2**31-1
                else:
                    return result * time

            if start:
                result *= 10
                result += ord(s[i]) - 48
        
        if result * time < -2**31:
            return -2**31
        elif result * time > 2**31-1:
            return 2**31-1
        else:
            return result * time

print("".strip())