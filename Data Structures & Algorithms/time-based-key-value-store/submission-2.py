class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timemap[key]) - 1
        arr = self.timemap[key]
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return res