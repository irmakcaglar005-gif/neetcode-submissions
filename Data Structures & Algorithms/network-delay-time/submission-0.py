class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges= collections.defaultdict(list)

        #lets create and adj list
        for u,v,w in times:
            edges[u].append((v,w))

        minHeap=[(0,k)]# starting node

        visit= set() #mark the visited

        t=0 # t is the result

        while minHeap:
            # we pop the weight and the node
            w1,n1= heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t= max(t,w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))
        #if every node is visited
        return t if len(visit)==n else -1
        