class TimeMap:

    def __init__(self):
        self.kvStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        return self.binarySearch(self.kvStore[key], timestamp)
    def binarySearch(self, vals: list[str], target: int):
        l = 0
        r = len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] == target:
                return vals[m][0]
            elif target > vals[m][1]:
                l = m + 1
            else:
                r = m - 1
        # at this point r will be on closest timestamp < target, so if it exists we can return that
        return vals[r][0] if r >= 0 else ""
        
