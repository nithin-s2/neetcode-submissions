class TrieNode:
    __slots__ = ["children", "word_end"]
    def __init__(self):
        self.children = {}
        self.word_end = False

class PrefixTree:
    __slots__ = ["head"]

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        cur  = self.head
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word_end = True

    def search(self, word: str) -> bool:
        cur = self.head
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.word_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True
        
        