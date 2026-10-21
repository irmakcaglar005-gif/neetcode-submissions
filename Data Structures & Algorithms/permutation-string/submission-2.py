class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation = {}

        for i in range(len(s1)):
            permutation[s1[i]] = 1 + permutation.get(s1[i], 0)

        window = {}
        l = 0

        for r in range(len(s2)):

            # Step 1: Add s2[r] to window
            window[s2[r]]= 1+ window.get(s2[r],0)

            # Step 2: If window size > len(s1),
            # remove the leftmost character
            if (r-l+1)> len(s1):
                window[s2[l]]-=1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

            # Step 3: Compare dictionaries
            if window==permutation:
                return True
            # If equal, return True

        return False