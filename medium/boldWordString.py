from typing import List


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        bold_index = {}
        answer = []
        closing = None

        for word in words:
            for i in range(len(s) - len(word) + 1):
                if s[i:i + len(word)] == word:
                    bold_index[i - 1] = max(i - 1 + len(word), bold_index.get(i - 1, -10))

        if -1 in bold_index:
            answer.append("<b>")
            closing = bold_index[-1]

        for i in range(len(s)):
            if i in bold_index:
                if closing == None:
                    answer.append(s[i])
                    answer.append("<b>")
                    closing = bold_index[i]
                elif closing != None and bold_index[i] > closing:
                    closing = bold_index[i]
                    answer.append(s[i])
                else:
                    answer.append(s[i])
            elif i == closing:
                answer.append(s[i])
                answer.append("</b>")
                closing = None
            else:
                answer.append(s[i])

        return "".join(answer)