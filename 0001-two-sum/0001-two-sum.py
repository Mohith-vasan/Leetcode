class Solution(object):
    def twoSum(self, nums, target):
        numToInd = {}
        for i in range(len(nums)):
            if target - nums[i] in numToInd:
                return [numToInd[target - nums[i]], i]
            numToInd[nums[i]] = i
        return []