class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:

    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        curr = self.root
        for let in word:
            if let not in curr.children:
                curr.children[let] = Trie()
            curr = curr.children[let]
            curr.count += 1

    def prefixCount(self, words: List[str], pref: str) -> int:
        curr = self.root

        for word in words:
            self.insert(word)

        for let in pref:
            if let not in curr.children:
                return 0
            curr = curr.children[let]

        return curr.count






        