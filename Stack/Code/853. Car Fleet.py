'''
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        dictV = {}
        for i in range(n):
            dictV[position[i]] = (target - position[i]) / speed[i]

        dictV = dict(sorted(dictV.items(), key = lambda x : -x[0]))

        stack = []
        x = 0
        for i in dictV:
            if len(stack) == 0:
                stack.append([dictV[i]])
            else:
                if dictV[i] <= stack[-1][0]:
                    stack[-1].append(dictV[i])
                else:
                    x += 1
                    stack.append([dictV[i]])

        return len(stack)

    