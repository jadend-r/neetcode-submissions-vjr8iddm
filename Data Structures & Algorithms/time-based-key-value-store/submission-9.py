class TimeMap:
    #use hashmap to map keys: [(val, timestamp)]
    #get method
        #brute force: linear scan on key's values picking first k, v 
            #pair w/ timestamp <= timestamp O(values)
        #optimize get() with binary search on values
            #to find k, v <= timestamp O(log values)
    def __init__(self):
        self.valueStore = {} #O(n * m) space

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.valueStore:
            self.valueStore[key] = []
        self.valueStore[key].append((value, timestamp))

    # O(log max(values))
    def get(self, key: str, timestamp: int) -> str:
        #binary search on the key values
        if key not in self.valueStore: return ""
        l, r = 0, len(self.valueStore[key]) - 1
        res = ""
        while l <= r:
            m = (r + l) // 2
            val, ts = self.valueStore[key][m]
            if ts == timestamp:
                res = val
                break
            elif ts < timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1
        return res

    # valueStore = {"alice": (happy, 1)}
      #get alice 1 -- l = 0, r = 0, m= 0 val, ts = happy, 1
      #get alice 2 -- l = 1, r = 0, m = 0, val, ts = happy, 1
    # valueStore = {"alice": (happy, 1), (sad, 3)}
      #get alice 3 -- l = 0, r = 1, m = 0, val, ts = happy, 1
        #          -- l = 1, r = 1, m = 1, val, ts = sad, 3

