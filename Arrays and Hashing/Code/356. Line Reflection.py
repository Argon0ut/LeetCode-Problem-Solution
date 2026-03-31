from typing import List
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        elems = set()
        minx = float('INF')
        maxx = float('-INF')

        for p in points:
            if tuple(p) not in elems:
                elems.add(tuple(p))

            minx = min(minx, p[0])
            maxx = max(maxx, p[0])

        y = (maxx + minx) / 2

        for p in points:
            if p[0] > y:
                if (p[0] - 2 * (p[0] - y), p[1]) not in elems:
                    return False
            elif p[0] == y:
                continue
            else:
                if (p[0] + 2 * (y - p[0]), p[1]) not in elems:
                    return False

        return True

