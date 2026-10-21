class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, ...]
        rob1,rob2 = 0,0

        #iterate thourough each of the houses we can rob
        for n in nums:
            #If we rob n, we can't rob the previous house. So we   combine it with rob1 : n+rob1 
            # if we don't rob the current house(n). we keep the best we already have: rob2
            temp = max(n + rob1, rob2)
            rob1=rob2
            rob2=temp
        return rob2