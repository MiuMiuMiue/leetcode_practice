class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        pairs = {
            "(": ")", 
            "{": "}", 
            "[": "]"
        }

        pair_stack = []

        for char in s:
            if char in pairs.keys():
                pair_stack.append(char)
            else:
                if not pair_stack:
                    return False
                last = pair_stack.pop()
                if char != pairs[last]:
                    return False
        
        if pair_stack:
            return False
                
        return True
