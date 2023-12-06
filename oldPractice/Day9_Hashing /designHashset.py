class MyHashSet:

    def __init__(self):
        self.mySet = []
        

    def add(self, key: int) -> None:
        if not key in self.mySet:
            self.mySet.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.mySet:
            self.mySet.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.mySet
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)