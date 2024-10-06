import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.nums.append(val)
        self.index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        if self.index[val] != len(self.nums) - 1:
            self.index[self.nums[-1]] = self.index[val]
            self.nums[self.index[val]] = self.nums[-1]

        self.nums.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()