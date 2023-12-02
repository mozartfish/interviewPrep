class Solution:
    # - create a unique hash key to group similar elements
    # return elements in the group
    def generateKey(self, st):
        result = [0 for i in range(26)]
        for ch in st:
            index = ord(ch) - ord('a')
            result[index] += 1
        # print(f"key: {result}") 
        return tuple(result)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} 
        for st in strs:
            key = self.generateKey(st)
            if key not in result:
                words = [st]
                result[key] = words 
            else:
                words = result[key]
                words.append(st)
                result[key] = words 
        
        values = result.values() 
        return list(values)



        