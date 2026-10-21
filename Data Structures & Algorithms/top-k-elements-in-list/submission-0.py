class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #hash map to count the occurences of each val
        freq= [[] for i in range(len(nums)+1)] 
        #the number of empty arrays is the size of our input +1
        #special array that is the same size as the input array
        #index is going to be the freq
        # value list of values that occur that particular number of times
        #this is bucket sort
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():   
        #will return the key-value pair we added to our dict 
            freq[c].append(n) # the value n occurs c times

        res= []    
        for i in range(len(freq)-1,0,-1):
            #because we want to start from the highest freq
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

    # O(n)                