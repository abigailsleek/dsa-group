class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #use a set to prevent duplicates
        duplicate = set()
        #loop through each item in the list
        for i in nums:
            if i in duplicate:
                return True
            duplicate.add(i)
        return False
            