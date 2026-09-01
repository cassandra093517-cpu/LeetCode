class Solution(object):
    def maxArea(self, height):
        
        res=0
        x,y=0,len(height)-1

        while x<y:
            size=(y-x)*min(height[x], height[y])
            res=max(res, size)

            if height[x]<height[y]:
                x+=1
            else:
                y-=1
            
        return res
        