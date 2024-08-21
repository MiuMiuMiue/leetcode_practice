class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        while len(a) < length:
            a = "0" + a
        while len(b) < length:
            b = "0" + b
        
        one = 0
        result = ""
        i = length - 1

        while i >= 0:
            num_a, num_b = int(a[i]), int(b[i])
            current = num_a + num_b + one
            if current == 3:
                result = "1" + result
                one = 1
            elif current == 2:
                result = "0" + result
                one = 1
            else:
                result = str(current) + result
                one = 0
            i -= 1
        
        if one:
            result = "1" + result
        
        return result
            
        