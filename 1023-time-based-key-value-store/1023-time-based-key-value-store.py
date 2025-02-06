class TimeMap:

    def __init__(self):
        self.store  = {}

    def set(self, key:str, val:str, timestamp:int):
        if key not in self.store.keys():
            self.store[key] = []
        self.store[key].append([val, timestamp])
    
    def get(self, key:str, timestamp:int) -> str:
        res = ""
        vals = self.store.get(key, [])

        l = 0
        r = len(vals)-1

        while l<=r:
            m = l + (r-l)//2

            if vals[m][1]>timestamp:
                r = m - 1
            else:
                res = vals[m][0]
                l = m + 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)