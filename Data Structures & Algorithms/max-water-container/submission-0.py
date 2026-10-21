class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #O(n)--> two pointer technique
        #we want the width to be as big as possible
        max_area=0
        l=0
        r=len(heights)-1

        while l<r:
            curr_area= (r-l)*(min(heights[l], heights[r]))
            max_area= max(max_area, curr_area)
            
            if heights[l]< heights[r]:
                l+=1
            #elif height[r]<height[l]:
                #r-=1
            else:
                r-=1
        return max_area
