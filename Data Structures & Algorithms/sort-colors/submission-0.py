class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #traverse
        for i in range(len(nums)):
            key=nums[i]
            j=i-1
            #compare and swap
            while j>=0 and nums[j]>=key:
                nums[j+1] =nums[j]
                j-=1
            nums[j+1]=key