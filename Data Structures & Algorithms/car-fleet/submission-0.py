class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n log n --> makes me think sorting

        # can sort positions to determine "fleets". Once sorted, can treat like a monotonic stack:
        # If top element can "overtake" leading fleet, pop the element. To determine if we can overtake,
        # treat like a linear equation where speed = m and pos = b: m1x + b1 = m2x + b2 and see if x is 
        # leq target ?
        # If it cannot overtake, add one to num fleets and let that be the new bench mark to overtake?

        # ok real optimal sol'n (i'm stupid again)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleet = 0
        max_time = 0
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # if front car reaches it before this car, set this one to be a new leader of a fleet.
            if time_to_target > max_time:
                fleet += 1
                max_time = time_to_target
        return fleet

        