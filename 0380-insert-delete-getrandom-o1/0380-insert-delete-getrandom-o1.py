import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            lastElement = self.list[-1]
            self.list[idx] = lastElement
            self.list.pop()
            self.dict[lastElement] = idx
            del self.dict[val]
            return True

        return False 
        

    def getRandom(self) -> int:
        return random.choice(self.list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()