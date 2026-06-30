# Assignment: HW11
# File: WordleAssistant.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 11.14.25
# Description of Program: 

# Imports

# Global constants

# Function definitions
def has_duplicates(word):
  return len(set(word)) < len(word)

def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair."""
    file_handle = open(filename,'r')
    word_list = [word[:len(word)-1] for word in file_handle.readlines()]
    filtered_word_list = []
    for word in word_list:
        if len(word) == 5 and has_duplicates(word) == False and word[-1] != 's':
            filtered_word_list.append(word)
    return filtered_word_list, len(filtered_word_list)

def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include. 
    """
    return set([word for word in wordlist if set(include) <= set(word)])

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude. 
    """
    return set([word for word in wordlist if set(word) & set(exclude) == set()])

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    output = set()
    for word in wordlist:
        match = True
        for letter, pos in posInfo.items():
            if word[pos] != letter:
                match = False
                break
        if match:
            output.add(word)
    return output


def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    pos_words = containsAtPositions(wordlist, posInfo)
    all_words = containsAll(pos_words, include)
    none_words = containsNone(all_words, exclude)
    return none_words