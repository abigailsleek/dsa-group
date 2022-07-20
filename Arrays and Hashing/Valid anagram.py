class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #handle cases where the lenght of strings are not equal
        if len(s) != len(t):
            return False
        #create hashmaps to store values of each letter of the given strings
        
        hashS, hashT = {}, {}
        for i in range(len(s)):
                hashS[s[i]] = 1 + hashS.get(s[i], 0)
                hashT[t[i]] = 1 + hashT.get(t[i], 0)
        for k in hashS:
            if hashS[k] != hashT.get(k,0):
                return False
        return True
