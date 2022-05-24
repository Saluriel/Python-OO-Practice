"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine to read a list of words and return how many words are in the file.  Will also pick a random word from the file.
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    
    def __init__(self, path):
        """Initialize the path and the list variables"""
        self.path = path
        self.word_list = []
    
    def __repr__(self):
        """Returns how many words were read from the file"""
        file = open(self.path, "r")
        words = file.read()
        word_list = words.splitlines()
        file.close()
        return f"{len(word_list)} words read"
    
    def random(self):
        """Returns a random word from the file"""
        file = open(self.path, "r")
        words = file.read()
        word_list = words.splitlines()
        file.close()
        print(random.choice(word_list))

class SpecialWordFinder(WordFinder):
    """Machine that will remove comments and empty lines from lists"""

    def __init__(self, path):
        super().__init__(path)

    def __repr__(self):
        """Returns the list with no spaces, empty lines, or comments"""
        file = open(self.path, "r")
        words = file.read()
        word_list = words.splitlines()
        file.close()
        no_spaces = list(filter(None, word_list))
        no_extras = [x for x in no_spaces if not x.startswith('#')]

        return f"{no_extras}"

    def random(self):
        """Returns a random item on the list excluding empty lines and comments"""
        file = open(self.path, "r")
        words = file.read()
        word_list = words.splitlines()
        file.close()
        no_spaces = list(filter(None, word_list))
        no_extras = [x for x in no_spaces if not x.startswith('#')]
        return(random.choice(no_extras))