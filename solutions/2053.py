class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            distinct_flag = True
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == arr[j]:
                    distinct_flag = False
            if distinct_flag:
                k -= 1
                if k == 0:
                    return arr[i]
        return ""