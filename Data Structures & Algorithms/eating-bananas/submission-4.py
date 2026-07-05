import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Our minimum k will assume that all the bananas are in one pile (ideal scenario)
        min_k = math.ceil(sum(piles) / h)
        # our max k will choose the pile with the greatest # of bananas
        # (since h always >= m)
        max_k = max(piles)

        L = min_k
        R = max_k
        cur_valid = -1
        while L <= R:
            # rate we are checking
            center = int(L + (R - L) / 2)

            hrs = 0
            # determine hours necessary
            for pile in piles:
                hrs += math.ceil(pile / center)
                if hrs > h:
                    break
            
            if hrs > h:
                L = center + 1
            elif hrs <= h:
                cur_valid = center
                R = center - 1
        
        return cur_valid

                
