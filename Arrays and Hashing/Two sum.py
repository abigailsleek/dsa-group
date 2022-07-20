class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first solution
        # for i in range(len(nums)-1):
        #     firstNum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         secNum = nums[j]
        #         if firstNum + secNum == target:
        #             return [i, j]
                
        # return []
        
        #second solution
        #create a hashmap
        hashMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return
