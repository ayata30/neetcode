class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            #cant be a anagram since the strings arent equal

        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


#char is s[i] -- they key 
# when we see a char 



        
        
