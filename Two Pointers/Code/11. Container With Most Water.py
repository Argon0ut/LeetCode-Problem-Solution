'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container
'''


# goal is to find the container with the most water --> the largest area
# multiply x by y
# x = distance between two heights
# y = minimum height between two heights

# approach --> we can use two pointers logic
from typing import List
class Solution:
    def maxArea(self, height : List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            currArea = min(height[l], height[r]) * (r - l)
            res = max(res, currArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

# max = 35
#
#   0 1 2 3 4 5 6 7 8 9 10
#   1 0 0 0 4 7 7 4 9 2 8

                        12
                      6 x
                    x 6 x
                  3 x 6 x
                0 3 x 6 x
              x 0 3 x 6 x
            x x 0 3 x 6 x
          1 x x 0 3 x 6 x
        1 x x x 0 3 x 6 x
      1 x x x x 0 3 x 6 x
    x 1 1 1 1 1 1 1 1 1 1
            |         |
           4>1     n-1