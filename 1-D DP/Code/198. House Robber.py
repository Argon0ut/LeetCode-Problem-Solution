from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [nums[0], nums[1]]

        if len(nums) < 3:
            return max(nums)

        res = max(memo)

        for i in range(2, len(nums)):
            to_add = max(memo[: i - 1])
            memo.append(nums[i] + to_add)
            res = max(res, memo[-1])

        return res
