from typing import List

class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        arr = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0

            if arr[i] != -1:
                return arr[i]

            arr[i] = nums[i] + min(dfs(i + 1), dfs(i + 2))
            return arr[i]

        return min(dfs(0), dfs(1))