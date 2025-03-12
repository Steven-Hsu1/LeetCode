class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        l = 0
        numWhite = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                numWhite += 1
            if r - l + 1 == k:
                res = min(res, numWhite)
                if blocks[l] == 'W':
                    numWhite -= 1
                l += 1
        return res