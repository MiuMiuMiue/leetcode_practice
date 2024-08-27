from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for level in range(1, numRows):
            current = []
            for i in range(level + 1):
                print(i)
                if i == 0 or i == level:
                    current.append(1)
                else:
                    current.append(triangle[level - 1][i - 1] + triangle[level - 1][i])
            triangle.append(current)
            print(triangle)
        
        return triangle

if __name__ == "__main__":
    A = Solution()
    print(A.generate(5))