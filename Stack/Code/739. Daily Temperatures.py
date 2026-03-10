'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        less = []

        for i in range(1, n):
            if temp[i] > temp[i - 1]:
                ans[i - 1] = 1
                toCut = []
                for t in range(len(less)):
                    if less[-1 - t][0] < temp[i]:
                        toCut.append(len(less) - 1 - t)
                        ans[less[-1 - t][1]] = i - less[-1 - t][1]

                    else:
                        break
                for idx in sorted(toCut, reverse=True):
                    less.pop(idx)

            else:
                less.append([temp[i - 1], i - 1])

        return ans
    