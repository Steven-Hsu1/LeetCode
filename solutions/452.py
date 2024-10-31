class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        minArrows = 1
        points.sort(key = lambda x: x[0])
        x = points[0][1]
        for balloon in points:
            if balloon[0] > x:
                minArrows += 1
                x = balloon[1]
            else:
                x = min(x, balloon[1])
        return minArrows


