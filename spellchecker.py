#!/usr/bin/python3
""" Main file with Handler class """
# pylint: skip-file
import sys
import inspect
from src.node import Node
from src.trie import Trie
from src.exceptions import SearchMiss


class SpellChecker:
    """Spellchecker class """
    _OPTIONS = {
        "1": "check_a_word",
        "2": "word_suggestion",
        "3": "change_dictionary",
        "4": "print_words",
        "5": "delete_word",
        "6": "quit"
    }

    def __init__(self):
        """ Initialize class """
        self.trie = Trie()
        self.trie.add_file_to_trie()

    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])

    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in sorted(self._OPTIONS):
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def check_a_word(self):
        """
        Check a word in current dictionary
        """
        try:
            word = input("\nEnter word to check spelling: \n>>> ")
            if self.trie.check_word(word):
                print("word is spelled correctly")
        except SearchMiss:
            print("word does not exist")

    def word_suggestion(self):
        """
        Get a word suggestion
        """
        old_substring = input(
            "\nEnter three letters then one letter at the time: \n>>> ")
        if len(old_substring) == 3:
            words = self.trie.check_substring(old_substring)
            for word in words:
                print(word)
        elif old_substring in ("quit", "q", "Q"):
            self.main()
        else:
            old_substring = ""
            print("Please enter three letters")

        while True:
            new_substring = input(
                "\nEnter more letters or quit to exit: \n>>> {}".format(old_substring))
            if new_substring in ("", " "):
                print("You need to add a letter")
                continue
            elif new_substring in ("quit", "q", "Q"):
                break
            old_substring += new_substring
            words = self.trie.check_substring(old_substring)
            if words == []:
                old_substring = ""
                print("Nothing found")
                break
            if words[0] == old_substring and len(words) == 1:
                print(words[0])
                print("All words found")
                break
            else:
                for word in words:
                    print(word)

    def change_dictionary(self):
        """
        Change dictionary
        """
        dict = input("\nEnter dictionary to be used: \n>>> ")
        try:
            self.trie.change_textfile(dict)
            print("Switched to " + dict)
        except FileNotFoundError:
            print("Invalid filename")

    def print_words(self):
        """
        Print all words in dictionary
        """
        self.trie.print_words()

    def delete_word(self):
        """
        Delete a word from dictionary
        """
        try:
            while True:
                word = input("\nEnter word to be deleted: \n>>> ")
                if word in ("", " "):
                    print("Please enter a word")
                    continue
                else:
                    self.trie.delete_word(word)
                    print("Deleted " + word)
                    return " "
        except SearchMiss:
            print("word is missing")

    @staticmethod
    def quit():
        """ Quit the program """
        sys.exit()

    def main(self):
        """ Start method """
        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")

            input("\nPress any key to continue ...")


if __name__ == "__main__":
    h = SpellChecker()
    h.main()
