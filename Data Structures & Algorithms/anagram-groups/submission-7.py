class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs: # go through everystring in the input
            count= [0] * 26 # a ... z ( in zero for each char)
            for c in s: # go through each char in a string
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)

        return list(res.values())