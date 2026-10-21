class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {},{}
        if len(s)!=len(t):
            return False
        #building the hash maps    
        # go through the keys of the strings at the same time
        for i in range(len(s)):
            # we are creating the keys
            # if it already exist, we increment it by 1
            countS[s[i]]=1+ countS.get(s[i],0)
            countT[t[i]]=1+ countT.get(t[i],0)

        #iterating through the hash maps
        # iterating through all of the key vals 
        #in one of the hash maps
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False   
        return True        




