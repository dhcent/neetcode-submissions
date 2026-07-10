class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # populate the frequency list with frequencies of the first string
        # Sliding window with L,R at 0. If the element at R's frequency is 0, move left pointer
        # to that val. If not 0 then is 2nd frequency lsit at R greater? if so also move left pointer.
        # If frequency lists are equivalent, return true.
        # i
        f_list1 = [0] * 26
        f_list2 = [0] * 26

        for c in s1:
            f_list1[ord(c) - ord('a')] += 1
        L,R = 0,0
        while R < len(s2):
            # determine idx
            idx = ord(s2[R]) - ord('a')
            f_list2[idx] += 1
            if f_list1 == f_list2:
                return True
            if f_list1[idx] == 0 or f_list1[idx] < f_list2[idx]:
                L += 1
                R = L
                f_list2 = [0] * 26
            else:
                R += 1

        return False
        
