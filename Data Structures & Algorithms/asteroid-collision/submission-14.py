class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # keep adding asteroids to the stack. destroy 
        stack = []
        for aster in asteroids:
            if stack and stack[-1] > 0 and aster < 0:
                while stack and stack[-1] * aster < 0:
                    broken = False
                    if abs(aster) < abs(stack[-1]):
                        broken = True
                        break
                    elif abs(aster) == abs(stack[-1]):
                        broken = True
                        stack.pop()
                        break
                    else:
                        #don't break asteroid
                        stack.pop()
                if not broken:
                    stack.append(aster)
            else:
                stack.append(aster)
        return stack