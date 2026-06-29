class Solution:
    def isValid(self, s: str) -> bool:
        # Create a hashmap that maps open brackets to close brackets
        # Whenever we see a open bracket, add that to our "array" which will act as a stack
        # whenever we see a close bracket, determine if that close bracket corresponds to our
        # open bracket. if it does, pop the open bracket. If it doesn't, return false.
        
        mp = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        for c in s:
            # no need to convert to list, dictionary view objects are highly optimized for look up O(1)
            if c in mp.keys():
                stack.append(c)
            else:
                # If stack is empty and you encounter a close bracket, return false.
                if len(stack) == 0:
                    return False
                    
                if mp.get(stack[-1]) == c:
                    stack.pop()
                else:
                    return False
        # Only return true if all complements have been found
        return stack == []