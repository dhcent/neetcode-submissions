class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Iterate through strs. For each letter in strs, add one to a size 26
        # array depending on letter index. Create a hashmap that maps letter fre
        # -quencies to word. If that array DNE, add it to the hashmap and set 
        # the key to a list with just that word. If that array exists, add word
        # to hashmap

        # T.C is O(m * n) where m is longest word in strs and n is len(strs)

        anagram = {}
        letter_frequency = [0] * 26 # array to store letter frequency in each word
        for word in strs:
            for char in word:
                letter_idx = ord(char) - ord('a') # a is 0, z is 25
                letter_frequency[letter_idx] += 1
            
            # .get fallback to 0 if letter freq DNE. If DNE, create the list w/ 
            # just the word. otherwise append word to that list.
            # note: dictionary keys must be immutable. Cannot simply use list/set,
            # must use tuple.
            cur = tuple(letter_frequency)
            if anagram.get(cur, 0) != 0:
                anagram[cur].append(word)
            else:
                anagram[cur] = [word]
            
            letter_frequency = [0] * 26 # reset for each word
        # .values() returns as "dict values view object" -- supposedly O(1)
        return list(anagram.values())