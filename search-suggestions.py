#create a new TrieNode class
class TrieNode:
    def __init__(self):
        self.children = OrderedDict()
        self.words = []

#trie class with ability to search as well as insert
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            node.words.append(word)
            node.words.sort()
            if len(node.words) > 3:
                node.words.pop()

    def search(self, word):
        node = self.root
        payload = []
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
                payload.append(node.words)
            else:
                for i in range(len(word) - len(payload)):
                    payload.append([])
                break
        return payload

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.search(searchWord)











