class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #bottom up approach
        # dp[i][curr_sum]=count --> cursum=0
        dp= [defaultdict(int) for _ in range(len(nums)+1)] #maps the sum to count
        dp[0][0]=1 # (0 elements, 0 sum) -> 1 way
        # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]]+= count
                dp[i+1][cur_sum - nums[i]]+= count
                
        return dp[len(nums)][target]
    













