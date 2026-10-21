class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent= [i for i  in range(n)]
        rank = [1] * n 

        def find(n1): # we want to find its root parent
            res=n1
            while res != parent[res]: # while result is not equal to the parent of itself
                parent[res]=  parent[parent[res]]
                res= parent[res]
            return res

        def union (n1, n2): #union their comp together
            p1, p2= find(n1), find(n2) # we want to get their parents 
            if p1==p2: # if their parents are the same
                return 0 # we did not perform a union
            if rank[p2]> rank[p1]: # p2 is going to be the parent of p1 because its rank is greater
                parent[p1]= p2 # set p2 to be the parent of p1
                rank[p2]+= rank[p1] # we added children to it
            else:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            return 1 # we did perform a succesful union
        res=n
        for n1, n2 in edges:
            res-= union(n1, n2)
        return res
            # everytime we succesfully perform a union operation, we decrement the num of compenents by 1. 
        