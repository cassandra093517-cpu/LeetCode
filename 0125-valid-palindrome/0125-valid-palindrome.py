class Solution(object):
    def isPalindrome(self, s):
        i,j=0,len(s)-1

        while i<j:
            while i<j and not self.isAlphaNum(s[i]):
                i+=1
            
            while j>i and not self.isAlphaNum(s[j]):
                j-=1
            
            if s[i].lower()!=s[j].lower():
                return False
            
            i,j=i+1,j-1

        return True
      
  
    
    
    def isAlphaNum(self, c):
        return (ord('a')<=ord(c)<=ord('z') or
        ord('A')<=ord(c)<=ord('Z') or
        ord('0')<=ord(c)<=ord('9')        
        )
        