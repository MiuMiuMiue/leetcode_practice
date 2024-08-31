class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for current in columnTitle:
            result *= 26
            result += ord(current) - ord("A") + 1
        return result

if __name__ == "__main__":
    print(ord("B") - ord("A"))