class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False

        dp=set() 
        dp.add(0)
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()
            for t in dp:
                nextDP.add(t+nums[i]) #take
                nextDP.add(t) #skip
            dp=nextDP
        return True if target in dp else False

        
            #[1,5,11,5] target=11
            # 1 or 0:
                # if 1 target=11-1=10 then i=1
                #if 0 then target=11-0=11 and i =1
            #for t in subarray:
                # if t==target:
                    #return True
            #BOTTOM UP SOLUTION WORKING FROM THE BACK
                
