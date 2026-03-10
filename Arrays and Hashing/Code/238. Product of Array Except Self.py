class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute division of the total multiple will not work because there might be the division by zero
        # that is why we are using the prefix and suffix

        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res