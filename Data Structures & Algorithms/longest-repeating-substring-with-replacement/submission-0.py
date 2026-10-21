class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(26n)
        #create a hasmap to count the freq
        # windowlen-count of the most freq char <= k is the condition
        count= {}
        res=0 #longest subs
        l=0
        for r in range(len(s)):
            count[s[r]]= 1 + count.get(s[r],0)
            while (r-l+1) - max(count.values())> k:
                count[s[l]]-=1
                l+=1

            res=max(res, r-l+1)
        return res
