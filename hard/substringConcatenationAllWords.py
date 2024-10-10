from collections import defaultdict, Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLength = len(words[0])
        wordCheck = dict(Counter(words))
        subLength = len(words) * wordLength
        answer = []

        for i in range(0, len(s) - subLength + 1):
            check = defaultdict(int)
            concat = True
            count = 0

            for j in range(i, i + subLength, wordLength):
                current_word = s[j:j + wordLength]
                if current_word in wordCheck:
                    check[current_word] += 1
                    if check[current_word] > wordCheck[current_word]:
                        concat = False
                        break
                    count += 1
                else:
                    concat = False
                    break

            if concat and count == len(words):
                answer.append(i)

        return answer

if __name__ == "__main__":
    A = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print(A.findSubstring(s, words))
