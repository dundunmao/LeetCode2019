from random import choice


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomized_hash = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.randomized_hash:
            self.randomized_hash[val].append(len(self.array))
            self.array.append(val)
            return False
        else:
            self.randomized_hash[val] = [len(self.array)]
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.randomized_hash:
            return False
        else:
            array_for_val = self.randomized_hash[val]
            val_index = array_for_val.pop()
            if len(array_for_val) == 0:
                self.randomized_hash.pop(val)
            if val_index == len(self.array) - 1:
                self.array.pop()
                return True
            self.array[val_index], self.array[-1] = self.array[-1], self.array[val_index]
            self.array.pop()
            self.randomized_hash[self.array[val_index]].remove(len(self.array))
            self.randomized_hash[self.array[val_index]].append(val_index)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.array)

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()

param_1 = obj.insert(10)
param_1 = obj.insert(10)
param_1 = obj.insert(20)
param_1 = obj.insert(20)
param_1 = obj.insert(30)
param_1 = obj.insert(30)

param_2 = obj.remove(10)
param_2 = obj.remove(10)
param_2 = obj.remove(30)
param_2 = obj.remove(30)

param_3 = obj.getRandom()


obj = RandomizedCollection()

param_1 = obj.insert(1)
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()



obj = RandomizedCollection()

param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()

["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
[[],[10],[10],[20],[20],[30],[30],[10],[10],[30],[30],[],[],[],[],[],[],[],[],[],[]]
