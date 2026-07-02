class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if len(stack) == 0:
                stack.append(time_to_target)
                continue
            if stack[-1] < time_to_target:
                stack.append(time_to_target)
        return len(stack)

        