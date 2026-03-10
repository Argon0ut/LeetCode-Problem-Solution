class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elems = {} #num: id
        for i in range(len(nums)):
            if target - nums[i] in elems:
                return [i, elems[target - nums[i]]]
            else:
                elems[nums[i]] = i