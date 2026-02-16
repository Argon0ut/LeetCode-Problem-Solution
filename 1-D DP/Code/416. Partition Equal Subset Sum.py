from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n % 2 == 1:
            return False

        target = n // 2
        memo = set()

        for i in range(len(nums)):
            if nums[i] == target:
                return True

            toAdd = [nums[i]]

            for j in memo:
                if j + nums[i] == target:
                    return True
                if j + nums[i] not in memo:
                    toAdd.append(nums[i] + j)

            for x in toAdd:
                memo.add(x)

        return False

