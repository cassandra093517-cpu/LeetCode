class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet=set(nums)
        list = 0

        for n in numSet:
            if (n-1) not in numSet:
                lgn=0
                while (n+lgn) in numSet:
                    lgn +=1

                list=max(lgn, list)
        return list
                
    