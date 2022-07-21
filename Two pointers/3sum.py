class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resArr = []
        nums.sort ()
        # loop through the index and value of each number in the list
        for i, val in enumerate(nums):
            # check for a case where the number is not the first number in 
            # the list and if it is the same as the number next to it
            if i > 0 and val == nums[i -1]:
                continue
            # use two pointer to iterate and compare numbers in the list
            left, right = i +1, len(nums) - 1
            while left < right :
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -=1
                elif threeSum < 0:
                    left += 1
                else:
                    resArr.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return resArr