class Solution:
    def climbStairs(self, n: int) -> int:
        #DP- bottom up
        #DP= [ ,x,x,x,x,next,one,two]
        one, two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one











