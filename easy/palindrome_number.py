class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)

        def check(number):
            if len(number) <= 1:
                return True
            if number[0] == number[-1]:
                return check(number[1:len(number) - 1])
            return False
        
        return check(num)

    def isPalindrome1(self, x: int) -> bool:
        num = str(x)
        if len(num) % 2 == 0:
            left = num[:len(num) // 2]
            right = num[len(num) // 2: len(num)]
            return left == right[::-1]
        else:
            left = num[:len(num) // 2]
            right = num[len(num) // 2 + 1:]

            return left == right[::-1]

if __name__ == "__main__":
    A = Solution()

    print(A.isPalindrome1(-121))