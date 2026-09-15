class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newS=[]
        
        for x in s:
            if x.isalnum():
                newS.append(x)
        
        i=0
        j=len(newS)-1

        while i<j:
            if newS[i]!=newS[j]:
                return False
            
            i+=1
            j-=1

        return True
        



        