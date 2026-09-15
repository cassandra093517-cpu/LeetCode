class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=dict()

        for x in s:
            if x in res:
                res[x]+=1
            else:
                res[x]=1
        
        for x in t:
            if x in res:
                res[x]-=1
            else: return False
        
        for x in res.values():
            if x !=0:
                return False

        return True  

        
        