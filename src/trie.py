""" Module for Trie """
from src.node import Node
from src.exceptions import SearchMiss
class Trie():
    """
    Class for Trie / Prefix tree
    """
    def __init__(self):
        self.root = Node()
        self.file = "dictionary"
        self.words = []
        self.trie = None

    def new_trie(self):
        """
        Create new Trie object
        """
        self.trie = Trie()

    def insert(self, word):
        """
        Create a node for each letter in word
        """
        node = self.root
        for idx, letter in enumerate(word):
            # if letter not in children
            if letter not in node.children:
                # make new Node
                prefix = word[0:idx+1]
                node.children[letter] = Node(prefix)
            # move pointer
            node = node.children[letter]
        # mark last node as end of word
        node.is_end = True

    def make_trie(self, words):
        """
        Make trie out of list of words
        """
        for word in words:
            self.insert(word)

    def add_file_to_trie(self):
        """
        Puts data from text file into trie
        """
        with open("./data/" + self.file + ".txt", "r", encoding='UTF-8') as fh:
            lines = fh.read()
            words = lines.splitlines()
            self.make_trie(words)

    def change_textfile(self, file):
        """
        Change text file
        """
        self.new_trie()
        self.file = file
        self.add_file_to_trie()

    def print_words(self):
        """
        Print the words from trie
        """
        print("Words in: " + self.file)
        words = self.get_all_words()
        for word in sorted(set(words)):
            print(word)

    def get_all_words(self):
        """
        Traverse trie and put words into list
        """
        self.__get_words(self.root, self.root.letter)
        return self.words

    def __get_words(self, node, prefix):
        """
        Find words in trie and put into a list
        """
        if node.is_end:
            # create a list of words
            self.words.append(node.letter)

        for letter in node.children:
            self.__get_words(node.children[letter], prefix + node.letter)

    def check_word(self, word):
        """
        Check if word in dictionary
        """
        node = self.root
        word = word.lower()
        for letter in word:
            if letter not in node.children:
                raise SearchMiss
            # move pointer
            node = node.children[letter]
        # check end of word
        if node.is_end:
            return True
        raise SearchMiss

    def check_substring(self, substring):
        """
        Check for substring in Trie and print matches
        """
        if substring == "":
            return "Please enter a substring"
        node = self.root
        self.words = []
        for letter in substring:
            if letter not in node.children:
                return self.words
            # move pointer
            node = node.children[letter]
        # create list with found words
        self.__get_words(node, substring[:-1])
        return self.words

    def delete_word(self, word):
        """
        Delete nodes by word
        """
        node = self.root
        self.__rec_delete_word(node, word, 0)
        return node

    def __rec_delete_word(self, node, word, index):
        """
        Check for word and delete it recursively
        """
        if self.check_word(word):
            letter = word[index]
            currentnode = node.children[letter]
            delete_node = False
            if currentnode is not None:
                #  word has the same prefix as the one to be deleted
                if len(currentnode.children) > 1:
                    self.__rec_delete_word(currentnode, word, index+1)
                    return delete_node
                # The string is a prefix of another string
                if index == len(word) - 1:
                    if len(currentnode.children) >= 1:
                        currentnode.is_end = False
                        return delete_node
                    node.children.pop(letter)
                    delete_node = True
                    return delete_node
                # word is the prefix of the string to be deleted
                if currentnode.is_end is True:
                    self.__rec_delete_word(currentnode, word, index+1)
                    return delete_node
                # No node depends on other word
                delete_node = self.__rec_delete_word(currentnode, word, index+1)
                if delete_node:
                    node.children.pop(letter)
                    return delete_node
            return delete_node
        raise SearchMiss

if __name__ == '__main__':
    trie = Trie()
    trie.add_file_to_trie()
