class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}

        for string in strs:
            key = "".join(sorted(string))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(string) 
        return list(anagram.values())