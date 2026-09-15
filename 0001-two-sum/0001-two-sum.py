class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        output = dict()

        for i, n in enumerate(nums):
            diff =  target-n
            if diff in output:
                return [output[diff],i]
            
            output[n]=i