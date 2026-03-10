class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all elements into a set
        # after that try to start looking for the consecutive elements
        # start lookup only from the elements that do not have the previous element in the set

        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                elem = num
                while elem in nums:
                    length += 1
                    elem += 1

                res = max(res, length)

        return res