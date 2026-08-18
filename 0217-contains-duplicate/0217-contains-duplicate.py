class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nonRepeat=set()
        for x in nums:
            if x in nonRepeat:
                return True
            else:
                nonRepeat.add(x)
        return False