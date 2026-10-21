import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles 
        #piles[i]= number of bananas in that pile. 
        #h = number of hours you have to eat all bananas.
        #k= banans-per-hour eating rate of k. 
        # if your pile has less than k bananas, you may finish eating the pile but cannot move to the next pile in the same hour.
        # return min k 
        l=1
        r= max(piles) #max element in the piles
        mid= (l+r)//2
    
        while l<=r:
            mid= (l+r)//2

            hours=0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours>h:
                l= mid+1
            else:
                r=mid-1
        return l 
                

