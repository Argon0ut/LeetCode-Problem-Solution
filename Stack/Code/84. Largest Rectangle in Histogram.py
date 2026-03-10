'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hDicts = {}
        for h in heights:
            if h not in hDicts:
                hDicts[h] = []

        for i in range(len(heights)):
            for h in hDicts:
                if h <= heights[i]:
                    hDicts[h].append(i)

        area = []
        for h in hDicts:

            n = len(hDicts[h])

            width = 1
            if n > 1:
                prev = hDicts[h][0]
                for i in range(1, len(hDicts[h])):
                    if hDicts[h][i] != -1 and (hDicts[h][i] - prev) <= 1:
                        prev = hDicts[h][i]
                        width += 1
                    else:
                        prev = hDicts[h][i]
                        print(h, width, 's')
                        area.append(h * width)
                        width = 1
                print(h, width)
                area.append(h * width)
            else:
                area.append(h)

        print(hDicts)
        print(area)
        return max(area)


