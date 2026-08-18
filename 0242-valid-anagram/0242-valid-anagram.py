class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        
        sNum, tNum={},{}

        for i in range(len(s)):
            sNum[s[i]] = 1+sNum.get(s[i],0)
            tNum[t[i]] = 1+tNum.get(t[i],0)
        
        for c in sNum:
            if sNum[c]!= tNum.get(c,0):
                return False
        
        return True