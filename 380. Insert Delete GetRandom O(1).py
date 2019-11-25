import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_set = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomized_set:
            return False
        self.array.append(val)
        self.randomized_set[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomized_set:
            return False
        self.randomized_set[self.array[-1]] = self.randomized_set[val]
        self.array[self.randomized_set[val]], self.array[-1] = self.array[-1], self.array[self.randomized_set[val]]
        self.array.pop()
        self.randomized_set.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.array[random.randint(0, len(self.array) - 1)]
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
