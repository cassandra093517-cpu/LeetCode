class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elem1=set(nums1)
        elem2=set(nums2)
        output = dict()
        res=[]

        for x in elem1:
            if x in output:
                output[x]+=1
            else: output[x]=1
        
        for x in elem2:
            if x in output:
                output[x]+=1
            else: output[x]=1
        
        for i, x in output.items():
            if x >1:
                res.append(i)
        
        return res


        