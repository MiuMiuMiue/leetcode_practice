class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        row_i = 0
        string_i = 0
        answer = ""

        while string_i < len(s):
            if row_i == numRows:
                row_i -= 2
                while row_i > 0 and string_i < len(s):
                    rows[row_i].append(s[string_i])
                    row_i -= 1
                    string_i += 1
            else:
                rows[row_i].append(s[string_i])
                row_i += 1
                string_i += 1
    
        for row in rows:
            answer += "".join(row)
        
        return answer
