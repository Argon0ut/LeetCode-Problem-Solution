'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.
'''

# memoizing the heights from left and right sides --> add two maximum trackers for left and right

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left, right = 0, n - 1

        lMx, rMx = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= lMx:
                    lMx = height[left]
                else:
                    water += lMx - height[left]
                left += 1
            else:
                if height[right] >= rMx:
                    rMx = height[right]
                else:
                    water += rMx - height[right]
                right -= 1
        return water    






