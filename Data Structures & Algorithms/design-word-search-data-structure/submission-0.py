class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.trie

        def helper(wordSub, currNode):
            tmp = currNode
            for i in range(len(wordSub)):
                if wordSub[i] == ".":
                    for child in tmp.children:
                        if child:
                            if helper(wordSub[i+1:], tmp.children[child]):
                                return True
                    return False

                else:
                    if wordSub[i] not in tmp.children:
                        return False
                    tmp = tmp.children[wordSub[i]]

            return tmp.end
    
        return helper(word, curr)








      


                
       







        
