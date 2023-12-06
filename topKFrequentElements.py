class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      '''
      - k starts at 1 -> 1 based counting 
      - runtime needs to be better than O(n log n) which means we can't use sorting
      Ideas 
      - use some kind of character count 
      - use some kind of 
      '''
      count = {} 
      freq = [[] for i in range(len(nums) + 1)]
      
      # map the number to its frequency count 
      for num in nums:
        count[num] = 1 + count.get(num, 0)
      
      # group numbers by their frequency count 
      for key, val in count.items():
        freq[val].append(key)

      # go through frequency groups and find the k number of most frequent items
      result = []
      for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
          result.append(num)
          if len(result) == k:
            return result 