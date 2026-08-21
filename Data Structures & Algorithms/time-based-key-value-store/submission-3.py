class TimeMap:

    def __init__(self):
        self.mapp = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapp[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""

        vals = self.mapp[key]

        l = 0
        r = len(vals)

        ans = -1
        
        while l < r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                ans = m
                l = m + 1
            else:
                r = m
        
        return vals[ans][0] if ans != -1 else ""