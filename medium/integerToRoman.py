class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {
            1: "I", 
            5: "V", 
            10: "X", 
            50: "L", 
            100: "C", 
            500: "D", 
            1000: "M"
        }

        roman = []

        time = 1
        while num > 0:
            current = num % 10
            if current < 4 and current > 0:
                roman.append(conversion[time] * current)
            elif current == 4:
                roman.append(conversion[time] + conversion[5 * time])
            elif current == 9:
                roman.append(conversion[time] + conversion[time * 10])
            elif current > 4:
                roman.append(conversion[5 * time] + conversion[time] * (current - 5))
            time *= 10
            num //= 10
        
        return "".join(roman[::-1])

