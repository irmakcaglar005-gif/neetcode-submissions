class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #creating the 2D grid
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i]==text2[j]: #chars match
                    dp[i][j]= 1+ dp[i+1][j+1]
                else: #dont match
                    dp[i][j]= max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]

        # time O(len(text1)*len(text2)) --> O(n*m) --> also the space
        