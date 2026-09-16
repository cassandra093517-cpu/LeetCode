class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        seen=set(nums)
        res=-1

        for x in seen:
            if x and -x in seen:
                res=max(res, x)

        return res