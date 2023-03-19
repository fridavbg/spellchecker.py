# Python Spellchecker

### Start app

```
python3 spellchecker.py
```

## Requirement 1: Foundation

In my implementation, I kept it to three files:

spellchecker.py contains the main program that receives user input and handles word output, Exceptions, and a menu with program options.

node.py is initiated in trie.py and represents a letter with a node. Depending on where the letter is in the tree, it also has a dictionary of the letter node's child nodes and a Boolean that marks whether it is the last letter in a word.

Then in trie.py, there are different methods that are called for different user inputs. For me, it was important to keep one method handling one thing, and I found it easier to separate the methods that used recursion.

I found it easiest to manage the different text files, where I use the insert method to create a node for each letter and thus build a new Trie when switching files.

I spent the most time on the recursive delete function that removes words from a dictionary. It took a while to get it right with base cases and moving the pointer correctly.

## Requirement 2: UML

My class diagram shows the three classes that I have used in my spellchecker: Node, Trie, and Spellchecker.

The methods in Trie are as I saw the requirements before I started, and I tried to predict whether I would use recursion or not. I also thought that I did not have a great need to have anything private, so everything in Trie is public. The diagram differs slightly from my code, as I later realized that I needed to use multiple recursive calls.

For my sequence diagram, I chose to show program choice 2 - Word Suggestion. The program has three lifelines: user, spellchecker, and Trie that go over the sequence of events when a user enters 3 letters and gets a list of words that start with those letters. Spellchecker first checks if the user has entered 3 letters, otherwise, the user is asked to submit a correct input. If correct input is entered, a list is displayed with the matching words, and then the user can enter more letters or choose to return to the main menu.

## Requirement 3 : Tests

For my testing, I have tried to think about what could go wrong. First, I create a trie structure with a few words to run the tests on. As the requirements mentioned that the program should be started with the dictionary.txt file, I chose to create a test for default values in trie first. My intention for the tests has also been to give a bigger picture of what each method in my Trie class does. For example, in the test_delete method, "hello" is removed and is not present in the word list when the program prints out all the words. I also test for the SearchMiss Exception to be thrown when a word is not in the word list.
