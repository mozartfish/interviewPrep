class Solution:
    # generate a unique key for anagram characters 
    # - loop through strings and map each word to the correct bucket and return the result 
    def generateKey(self, string): 
        result = [0 for i in range(26)]
        for ch in string:
            index = ord(ch) - ord('a') 
            result[index] += 1
        # print("result value", result)   
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