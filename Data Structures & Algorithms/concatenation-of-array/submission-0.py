class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ans.insert(i,nums[i])
            ans.insert(i+n,nums[i])
        return ans