class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #2D array for the base cases +1
        cache= [[float("inf")] * (len(word2)+ 1) for i in range(len(word1)+1)]
        #initialing the base cases of our 2 dim array
        for j in range(len(word2)+1):
            cache[len(word1)][j]= len(word2) - j
        for i in range(len(word1)+1):
            cache[i][len(word2)]= len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    cache[i][j]=cache[i+1][j+1]
                else: #check all three directions
                    cache[i][j]= 1+ min(
                        cache[i+1][j], #delete
                        cache[i][j+1], # insert
                        cache[i+1][j+1] #replace
                    )
        return cache[0][0]