from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap to map each count of the character to the list of Anagrams
        output = defaultdict(list)
        # loop through each item in the input list
        for s in strs:
            # initialized a count for al the small letter alphabets
            count = [0] * 26
            # loop through each character in the word contained in s and get the index
            for char in s:
                count[ord(char)- ord("a")] += 1
            output[tuple(count)].append(s)
        return output.values()
