class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      '''
      - array is already sorted in non-decreasing order 
      - index of numbers is 1 based -> need to add 1 in result 
      - there is exactly one solution 
      - cannot use the same element twice 
      - constant extra space 
      Ideas 
      - two pointers to get an O(n) runtime 
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