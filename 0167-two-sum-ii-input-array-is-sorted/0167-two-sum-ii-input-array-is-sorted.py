class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        res=[]
        i=0
        j=len(numbers)-1
        
        while i<j and numbers[i]+numbers[j]!=target:
            if numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                j-=1
        res=[i+1,j+1]
                
        return res

        


        