from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        conversion = {
            "2": "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        results = []

        def convert(digit_index, combination):
            if digit_index == len(digits):
                results.append(combination)
                return
            
            for char in conversion[digits[digit_index]]:
                convert(digit_index + 1, combination + char)
            
        convert(0, "")
        return results
