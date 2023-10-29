class TrieNode:
    def __init__(self):
        self.children = {} 
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        root = self.root 
        root.index = index 
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode() 
            root = root.children[c]
            root.index = index 

    def find(self, prefix, suffix):
        ps = suffix + '#' + prefix
        root = self.root 
        for c in ps:
            if c not in root.children:
                return -1 
            root = root.children[c]
        return root.index 

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie() 
        for index, word in enumerate(words):
            n = len(word)
            temp = word + '#' + word 
            for i in range(n):
                self.trie.insert(temp[i:], index)
        

    def f(self, pref: str, suff: str) -> int:
        return self.trie.find(pref, suff)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)