class TimeMap:
    def __init__(self):
        self.mapp = defaultdict(list) # {k : [[], [], []]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""
        valTime = self.mapp[key]
        best = ""
        l = 0 
        r = len(valTime)
        while l < r:
            m = (l + r) // 2
            if valTime[m][1] <= timestamp:
                l = m + 1
                best = valTime[m][0]
            else:
                r = m
        return best



        
        

        
        
