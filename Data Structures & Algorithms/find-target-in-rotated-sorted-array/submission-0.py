class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid= (l+r)//2
            if nums[mid]==target:
                return mid

            elif nums[mid]!= target:
                if nums[l]<=nums[mid]: #left sorted case
                    if nums[l]<=target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                if nums[r]>= nums[mid]: #right sorted case
                    if nums[r]>= target>nums[mid]:
                        l=mid+1
                    else:
                        r=mid-1

             #if not in list
        return -1

