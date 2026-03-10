'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:



-1 1 0 2 5 -7
-1 -7 0 1 2 5

O(n^3) time
O(n) space --> n size of the array





















class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []

        for i in range(length - 2):
            if i>0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while right > left:
                summation = nums[left] + nums[i] + nums[right]

                if summation == 0:
                    ans.append([nums[left], nums[i], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1


                elif summation > 0:
                    right -= 1
                else:
                    left += 1

        return ans
