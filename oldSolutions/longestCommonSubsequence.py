class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cols - len(text2)
        # row - len(text1)
        cache = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # print(cache)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # characters match 
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i + 1][j + 1]
                else:
                    cache[i][j] = max(cache[i][j + 1], cache[i + 1][j])
        
        return cache[0][0]
        