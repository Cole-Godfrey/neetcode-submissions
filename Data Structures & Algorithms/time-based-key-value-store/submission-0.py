class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        res = ""
        arr = self.hashmap.get(key, [])
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                # valid value to return
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
        
        
