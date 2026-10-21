class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp={}  #subarr piles (l,r) -> Max Alice Total
    
        def dfs(l,r): #return max alice total
            if l > r:#base case
                return 0 
            if (l,r) in dp:#base case
                return dp[(l,r)]

            # even number of elements remaning means alice is making the choice
            #odd number of elements remaning means bob is making the choice
            even= True if (r-1)%2 else False
            left= piles[l] if even else 0
            right= piles[r] if even else 0
            dp[(l,r)]= max(dfs(l+1,r) +left, dfs(l,r-1) + right )
            return dp[(l,r)]
        return dfs(0, len(piles)-1)> (sum(piles))//2