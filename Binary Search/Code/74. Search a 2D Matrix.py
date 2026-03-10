'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

# -x - 1
# -x ... y  --> matrix[x][-1] < matrix[x+1][0]

# first check if target is in specific range matrix[x][0] <= target <= matrix[x][m]
# basically we are going to implement two binary searches
# first --> finding specific row
# second --> finding specific element from that row
# n --> size of the matrix
# m --> size of the arrays in the matrix

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[right][0] > target:
                right = mid - 1
            elif matrix[left][-1] < target:
                left = mid + 1
            else:
                l = 0
                r = m - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        return True
        return False