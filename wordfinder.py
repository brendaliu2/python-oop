"""import random func/class"""
import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""


    """constructor"""
    def __init__(self, file_location):
        self.file_location = file_location
        """read a text file in python
        save the words in a list
        remove last 2 char for example cat\n"""
        file = open(self.file_location, 'r')
        text = file.readlines()
        file.close()
        print(str(len(text)) + " words read")

        """text should contain a list \n
        iterate over the word lst and append to lst """
        self.lst = []
        for word in text:
            self.lst.append(word[:-2])
        print("wordFinder", self.lst)


    """method random will return a random word from the list"""
    def random(self):
        return random.choice(self.lst)

wf = WordFinder("words.txt")
print(wf.random())

""" subclass will make a new list that removes # in front of words
 and removes empty lines"""
class SpecialWordFinder(WordFinder):
    def __init__(self, file_location):
        super().__init__(file_location)
        self.lst = list(filter(lambda word: (word != "" and word[0] != "#"), self.lst))


swf = SpecialWordFinder("words.txt")
"""prints a random word with parents method"""
print(swf.random())

