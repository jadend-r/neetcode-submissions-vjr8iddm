class TimeMap:

    def __init__(self):
        self.hm = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        values = self.hm[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                value = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return value
