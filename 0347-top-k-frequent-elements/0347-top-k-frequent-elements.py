class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        seq=[[]for i in range(len(nums)+1)]

        for n in nums:
            count[n]=count.get(n, 0)+1
        
        for n,c in count.items():
            seq[c].append(n)
        
        res=[]

        for i in range(len(seq)-1,0,-1):
            for n in seq[i]:
                res.append(n)
                if len(res) == k:
                    return res 