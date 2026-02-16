from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {0 : 1}
        res = 1

        for i in range(1, len(nums)):
            curr_max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] <= curr_max_len:
                        curr_max_len = dp[j] + 1

            dp[i] = curr_max_len
            res = max(res, curr_max_len)

        return res
