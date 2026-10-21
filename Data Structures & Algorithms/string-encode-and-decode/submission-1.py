class Solution:
    # we have list of strings and we want to encode it into a single string in O(n) time

    def encode(self, strs: List[str]) -> str:
        res=""
        # kelimeleri ayirmak icin her kelimenin basina uzunlugunu int seklinde yazip arkasina # isareti koyuyuroz. 
        # we are going to do this for every single input in the list then add it to the result
        for s in strs:
            res+= str(len(s))+ "#" + s
        return res
# this time we are given a single encoded string 
# now our result is going to be a list of strings
    def decode(self, s: str) -> List[str]:
        res,i= [], 0
        #i tell the position

        while i<len(s): # while i is still in bound we are going to read it char by char decoding each string
            j=i
            while s[j] != "#":
                j+=1
            length= int(s[i:j]) #now length tells us how many following chars we have to read after j in order to get every char of the string
            res.append(s[j+1 : j+1 + length])
            # now that we read the first word, we want to move to the next one, how are we going to do that?
            i= j + 1 + length # (beginning of the next string)
        return res






