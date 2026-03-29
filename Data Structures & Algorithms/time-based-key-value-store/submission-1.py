class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timemap[key]) - 1
        arr = self.timemap[key]
        while l < r:
            mid = (l + r) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return arr[l][0] if l <= len(self.timemap[key]) - 1 and arr[l][1] <= timestamp else ""
