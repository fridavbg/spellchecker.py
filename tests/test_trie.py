#!/usr/bin/env python3
""" Module for testing the class Trie """

import unittest
from src.trie import Trie
from src.node import Node
from src.exceptions import SearchMiss


class TrieTest(unittest.TestCase):
    """
    Testcases for Trie class
    """

    def setUp(self):
        """ Create Trie for tests """
        self.trie = Trie()
        self.trie.insert("hello")
        self.trie.insert("hi")
        self.trie.insert("good")
        self.trie.insert("bad")
        self.trie.insert("thing")
        self.trie.insert("yellow")
        self.trie.insert("spanish")
        self.trie.insert("help")
        self.trie.insert("helpful")

    def test_trie_default_values(self):
        """
        Test default values of a new Trie object
        """
        self.assertIsInstance(self.trie.root, Node)
        self.assertEqual(self.trie.file, "dictionary")
        self.assertIsInstance(self.trie.words, list)
        self.assertIsNone(self.trie.trie)

    def test_change_textfile(self):
        """
        Test to change testfile
        """
        self.trie.change_textfile("tiny_dictionary")
        self.assertEqual(self.trie.file, "tiny_dictionary")
        self.assertNotEqual(self.trie.file, "dictionary")

    def test_add_file_to_trie(self):
        """
        Test to put data from text file into trie
        """
        self.trie.add_file_to_trie()
        self.assertNotEqual(len(self.trie.root.children), {})
        self.assertIsNotNone(self.trie)
        self.assertEqual(len(self.trie.get_all_words()), 25404)

    def test_get_all_words(self):
        """
        Test to get all words from Trie
        """
        self.assertNotEqual(self.trie.get_all_words(), [])
        self.assertEqual(len(self.trie.words), 9)

    def test_check_word(self):
        """
        Test to check if word is in trie
        """
        self.assertTrue(self.trie.check_word("hello"))
        self.assertTrue(self.trie.check_word("help"))
        with self.assertRaises(SearchMiss):
            self.trie.check_word("Loud")
            self.trie.check_word("Metal")

    def test_check_substring(self):
        """
        Test to check for a substring in trie
        """
        self.assertEqual(self.trie.check_substring(
            'hel'), ['hello', 'help', 'helpful'])
        self.assertNotEqual(self.trie.check_substring("hel"), [])
        self.assertEqual(self.trie.check_substring('ghh'), [])

    def test_delete_word(self):
        """
        Test to delete node by word
        """
        self.trie.delete_word('hello')
        self.assertNotIn("hello", self.trie.get_all_words())
        with self.assertRaises(SearchMiss):
            self.trie.delete_word('green')
            self.trie.delete_word('grass')
