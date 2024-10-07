class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        current = ""

        for i in range(len(s) - 1, -1, -1):
            if current and s[i] == " ":
                answer += current[::-1] + " "
                current = ""
            elif s[i] != " ":
                current += s[i]
        
        if current:
            answer += current[::-1]
        else:
            answer = answer[:len(answer) - 1]

        return answer
    
