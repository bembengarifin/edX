# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    dict = {}
    
    #upper case
    i = 0
    for c in string.ascii_uppercase:
        dict[c] = string.ascii_uppercase[(i+shift)%len(string.ascii_uppercase)]
        i+=1

    #lower case
    i = 0
    for c in string.ascii_lowercase:
        dict[c] = string.ascii_lowercase[(i+shift)%len(string.ascii_uppercase)]
        i+=1

    #i = 0
    ##digits
    #for c in string.digits:
    #    dict[c] = string.digits[(i+shift)%len(string.digits)]
    #    i+=1    
            
    return dict        

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    encoded = ""
    for t in text:
        if coder.has_key(t):
            encoded += coder[t]
        else:
            encoded += t
    return encoded
            

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    #return "Not yet implemented." # Remove this comment when you code the function
    return applyCoder(text,  buildCoder(shift))   
    
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    declare best match shift
    declare best match total
    
    split the text by the space or punctuation 
    loop from 1 to 26
        if the first word is not in the word list then
            skip to next index
        else
            set match to 1
            for each word in the word list
                increment match
            if match is greater than best match total
                set best match shift to index

    return best match shift

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    #return "Not yet implemented." # Remove this comment when you code the function

    bestMatchShift = 0
    bestMatchTotal = 0
    
    cleanText = ""
    for t in text:
        if t in string.punctuation:
            continue
        else:
            cleanText += t

    words = cleanText.split(' ')
    
    if (len(words) > 0):
        for shift in range(0, 26):
            if isWord(wordList, applyShift(words[0], shift)):
                totalMatch = 1
                for w in words:
                    if isWord(wordList, applyShift(w, shift)):
                        totalMatch += 1
                if totalMatch > bestMatchTotal:
                    bestMatchShift = shift
            else:
                continue;
    
    return bestMatchShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    #return "Not yet implemented." # Remove this comment when you code the function
    wordList = loadWords()
    story = getStoryString()
    bestShift = findBestShift(wordList, story)
    return applyShift(story, bestShift)
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #print buildCoder(9)
    #print applyCoder("Hello, world!", buildCoder(3))
    #print applyCoder("Khoor, zruog!", buildCoder(23))
    #print applyShift('This is a test.', 8)
    #print applyShift('Bpqa qa i bmab.', 18)
    #print findBestShift('', '')
    #print string.ascii_uppercase    
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #print bestShift
    #assert applyShift(s, bestShift) == 'Hello, world!'
    #print findBestShift(wordList, 'TqxxA, Iadxp!')
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
