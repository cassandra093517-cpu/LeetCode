class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elem= dict()
        

        for x in nums:
            elem[x]=elem.get(x,0)+1
        
        for i in elem:
            elem[i]/=2
        
        res=max(elem, key=elem.get)

        return res


        