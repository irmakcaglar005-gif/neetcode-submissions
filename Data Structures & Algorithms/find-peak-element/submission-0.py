class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums,0, len(nums)-1)
    
    def search(self, nums, l, r):
        if l==r:
            return l
        mid = (l+r)//2
        if nums[mid]> nums[mid+1]:
            # search in the left array
            # there is already a possibility of a peak in the left array
            return self.search(nums,l,mid)
        #going up the hill
        return self.search(nums,mid+1,r)