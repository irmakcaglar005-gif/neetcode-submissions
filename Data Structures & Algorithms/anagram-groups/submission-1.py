class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)# mapping charCount to list of Anagrams

        for s in strs:
            count= [0]*26 # a...z
            #makes a list of 26 zeros [0,0,...,0]

            for c in s:
                #ord(x) gives the unicode number for a char
                #ord('a')= 97, b98,...
                count[ord(c) - ord('a')] +=1
                # ord(c) - ord('a') -> if c='a' -> 97-97=0
                #maps a letter to an index 0..25

            # in python lists cannot be keys 
            #so below we add the tuple()(tuples are nonmut)
            res[tuple(count)].append(s)   

        return list(res.values())  

        #optimal solution O(m*n)
        # m is the num of strs we are given
        # n is the avg length of each str
