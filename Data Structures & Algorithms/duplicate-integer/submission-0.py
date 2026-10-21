class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            elif nums[i] in seen:
                return True 
        return False           