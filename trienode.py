class TrieNode:
    def __init__(self):                            # Constructor 
        self.word = None
        self.children = {}
    def insert(self, word):                        # Function to pass new words in the trie 
        node = self
        for letter in word:                        # Loop to read every letter of the word
            if letter not in node.children:    
                node.children[letter] = TrieNode() # If letter not in children node, insert it
            node = node.children[letter]
        node.word = word                           # After every letter is finished in the word, create this word as a branch of tree.
