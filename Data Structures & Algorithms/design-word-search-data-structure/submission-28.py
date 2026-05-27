class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

        

    def search(self, word: str) -> bool:
        def dfs(node, j):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for n in node.children.values():
                        if dfs(n, i+1):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False    
                    node = node.children[c]
            return node.is_word

        return dfs(self.root, 0)
