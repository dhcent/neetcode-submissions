class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mp.get(key, -1) == -1:
            self.mp[key] = [(value, timestamp)]
        else:
            self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # gets a list of all the values and their corresponding timestamps
        # orchestrate binary search, but store the closest time stamp when searching
        # Whenever we shift our left index up, we have found a "smaller" timestamp 
        # that's valid
        if self.mp.get(key, -1) == -1: #return blank if key doesn't exist
            return ""
        vals = self.mp[key]
        prev_id = -1
        L = 0
        R = len(vals) - 1
        while L <= R:
            mid = L + (R - L) // 2
            cur_timestamp = vals[mid][1]
            # if you found the correct time stamp
            if cur_timestamp == timestamp:
                prev_id = mid
                break

            if cur_timestamp < timestamp:
                prev_id = mid
                L = mid + 1
            else:
                R = mid - 1
        if prev_id == -1:
            return ""
        return vals[prev_id][0]