from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        #Using hash table as a dp since the size of the dp is not fixed. If it was fixed we could use a list as a dp
        dp = {0:(nums[0], nums[0])}

        for i in range(1, len(nums)):
            w_prev, l_prev = dp[i-1]

            best = max(nums[i], nums[i] * w_prev, nums[i] * l_prev)
            worst = min(nums[i], nums[i] * l_prev, nums[i] * w_prev)

            dp[i] = (best, worst)
            res = max(res, best)

        return res
