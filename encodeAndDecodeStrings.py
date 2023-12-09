class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        - keep track of string length 
        - separate duplicate strings and unique characters 
        """
        result = ""
        for s in strs:
          result += str(len(s)) + "#" + s
        
        return result 
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0 
        while i < len(s):
          j = i
          # find length of string 
          while s[j] != "#":
            j += 1 
          length = int(s[i:j])

          # add string 
          string = s[j + 1:j + 1 + length]
          result.append(string)

          # update end of string 
          i = j + 1 + length
        
        return result 


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))