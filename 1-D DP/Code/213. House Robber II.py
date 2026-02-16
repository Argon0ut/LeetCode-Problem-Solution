from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo1 = [nums[0], nums[1]]
        res1 = max(memo1)

        memo2 = [0, nums[1]]
        res2 = nums[1]

        n = len(nums)

        for i in range(2, n):
            toAdd1 = max(memo1[: i - 1])
            if i != n - 1:
                memo1.append(nums[i] + toAdd1)
            res1 = max(res1, memo1[-1])

            toAdd2 = max(memo2[: i - 1])
            memo2.append(nums[i] + toAdd2)
            res2 = max(res2, memo2[-1])

        return max(res1, res2)
