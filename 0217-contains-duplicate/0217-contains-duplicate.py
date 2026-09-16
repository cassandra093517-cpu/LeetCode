class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=dict()
        for x in nums:
            seen[x]=seen.get(x,0)+1
        
        for x in seen.values():
            if x >1:
                return True
        
        return False
      