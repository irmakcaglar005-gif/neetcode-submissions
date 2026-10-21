class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #BUCKET SORT  
    #MAX frequency is length of the list
    #bucket index=frequency
        counts={}
        res=[]
        for num in nums:
            if num not in counts:
                counts[num]=1
            else:
                counts[num]+=1
        bucket= [[] for _ in range(len(nums)+1)]
        for key,value in counts.items():
            bucket[value].append(key)

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
