class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cols - text 2 
        # rows - text 1 
        text1Len = len(text1)
        text2Len = len(text2)
        cache = [[0 for j in range(text2Len + 1)] for i in range(text1Len + 1)]
        # print(cache)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
               
                # characters match 
                if text1[i] == text2[j]:
                    # move in a diagonal 
                    cache[i][j] = 1 + cache[i + 1][j + 1]
                else:
                    # move down or to the right
                    cache[i][j] = max(cache[i][j + 1], cache[i + 1][j])
        
        return cache[0][0]