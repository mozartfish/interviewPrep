class TimeMap:

    def __init__(self):
        # key - list of [val, timestamp]
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])
        return
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        # binary search 
        l = 0
        r = len(values) - 1 
        while l <= r:
            mid = (l + r) // 2 
            if values[mid][1] <= timestamp:
                # store the closest value to the value we are looking for 
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1 
        
        return result 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)