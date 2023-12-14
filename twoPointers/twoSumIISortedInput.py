class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        - 1 indexed array of integers -> need to add one to indices to correct value 
        - array is sorted in non-decreasing order 
        - find two numbers such that they add up to target value 
        - return indices of two numbers added by one as an integer array of length 2 -> [indx1, indx2]
        - cannot use same element twice 
        - must use only constant extra space 
        '''
        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] < target:
                L += 1 
            elif numbers[L] + numbers[R] > target:
                R -= 1 
            else:
                return [L + 1, R + 1]
                
        return []