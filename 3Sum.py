class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        - there can be no duplicate triples
        - sort the numbers and then apply Two sum II 
        '''
        result = []
        nums.sort() 
        for indx, val in enumerate(nums):
          # check for duplicates 
          if indx > 0 and val == nums[indx - 1]:
            continue 
          # two sum ii 
          L = indx + 1 
          R = len(nums) - 1 
          while L < R:
            total = val + nums[L] + nums[R]
            if total < 0:
              L += 1 
            elif total > 0:
              R -= 1 
            else:
              result.append([val, nums[L], nums[R]])
              # update one of the pointers
              L += 1 
              # check for duplicates again when we update L 
              while L < R and nums[L] == nums[L - 1]:
                L += 1 
        return result