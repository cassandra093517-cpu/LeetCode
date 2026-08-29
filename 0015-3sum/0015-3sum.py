class Solution(object):
    def threeSum(self, nums):
        result=[]
        nums.sort()

        for i,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
        
            x, y = i+1, len(nums)-1

            while x<y:
                sum= v+nums[x]+nums[y]
                if sum >0:
                    y-=1
                elif sum<0:
                    x+=1
                else:
                    result.append([v,nums[x],nums[y]])
                    x+=1
                    while nums[x]==nums[x-1] and x<y:
                        x+=1
        return result