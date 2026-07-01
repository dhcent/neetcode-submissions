class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Same idea as next greater element. Create a hashmap that maps days to num days till
        # greater temp appears. Use a stack ->
        # Add elements to stack if it is empty.
        # If stack non empty, compare element to top of stack. If element is warmer than top of stack,
        # that element is 1 day away and thus is added to the map with the index 1. Keep doing this
        # for future items until either stack is empty or temp is not sufficently warm. (increment idx)
        # by 1 each time.
        # for items left in the stack, set their map values to 0 to imply no  greater temp.

        # T.C O(n) since we do one pass to construct the hashmap, and another pass to generate result.
        # Can't use for each loop since we need to store index in the stack 

        # For each key in map, must store index as well to ensure we are accessing right element 
        # (temperatures are not distinct)

        stack = []
        # map should actually just map index to distance
        mp = {}
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not stack:
                stack.append([temp, i])
                continue
            while stack and stack[-1][0] < temp:
                cur = stack.pop() # cur is (temp, index)
                mp[cur[1]] = i - cur[1] #find distance between indexes.
            
            stack.append([temp, i])
        # for the left over indexes, set to 0
        for temp in stack:
            mp[temp[1]] = 0

        res = []
        for i in range(len(temperatures)):
            res.append(mp[i])
        return res
