class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numList={}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numList:
                return [numList[diff],i]
            numList[n]=i
        return []