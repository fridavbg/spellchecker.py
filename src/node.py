""" Module for Node class """

class Node:
    """
    Node class
    A node represents a letter and a dict of child nodes
    """
    def __init__(self, letter = ""):
        self.letter = letter
        self.children = {}
        self.is_end = False
