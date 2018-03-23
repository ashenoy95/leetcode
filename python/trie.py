class Node:
    def __init__(self):
        self.children = [None]*26
        self.end = False
        
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
        
    def getNode(self):
        return Node()
    
    def charToIndex(self, char):    #to store in children array
        return ord(char)-ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        parent = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])
            if not parent.children[index]:
                parent.children[index] = self.getNode()
            parent = parent.children[index]
        parent.end = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])
            parent = parent.children[index]
            if not parent:
                return False
        return parent.end
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent = self.root
        for i in range(len(prefix)):
            index = self.charToIndex(prefix[i])
            if not parent.children[index]:
                return False
            parent = parent.children[index]
        return True
            
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
