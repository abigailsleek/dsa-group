class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left  < right:
            checkSum = numbers[left] + numbers[right]
            #if the checkSum is greater than target, decrease the right by 1
            if checkSum > target:
                right -= 1

            #else,increase the pointer on the left by 1
            elif checkSum < target:
                left += 1
            else:
                return [left + 1, right + 1] 