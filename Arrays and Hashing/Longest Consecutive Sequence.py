class Solution:
    def longestConsecutive(self, nums:List[int])-> int:
        # create a set to hold values from the list
        valSet = set(nums)

        # initialize a count for the longest sequence.
        longest = 0
        
        # loop through each value in the nums list and check if it the start of the
        # the sequence

        for i in nums:
            if (i -1) not in valSet:
                length = 0
                while (i + length) in valSet:
                    length += 1
                longest =  max(length, longest)
        return longest


