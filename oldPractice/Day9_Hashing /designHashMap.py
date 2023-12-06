class MyHashMap:

    def __init__(self):
        self.size = 2069 
        self.map = [[] for i in range(self.size)]
    
    def hashFunc(self, key):
        return key % self.size
    
    def getIndex(self, key):
        hashVal = self.hashFunc(key)
        bucket = self.map[hashVal]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1

    def put(self, key: int, value: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            bucket.append((key, value))
        else:
            bucket[index] = (key, value)
        

    def get(self, key: int) -> int:
        bucket, index = self.getIndex(key)
        if index < 0:
            return -1 
        return bucket[index][1]
        

    def remove(self, key: int) -> None:
        bucket, index = self.getIndex(key)
        if index < 0:
            return 
        else:
            bucket.remove(bucket[index])
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)