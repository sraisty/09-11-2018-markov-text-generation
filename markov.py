"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text = file.read()

    # return 
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    # your code goes here
    words = text_string.split()

    # We look a the 3 words at list starting at words[i], 
    # so to make sure we don't look at items outside the list
    # we only loop to where words[i] is the second-to-last 
    # item in words
    for i in range(len(words) - 2):
        # create our tuple that will be a key for this key:value pair
        key = (words[i], words[i+1])
        # if this tuple is already in the dictionary, get the list of 
        # nextwords that are its value. 
        next_word = chains.get(key, [])
        next_word.append(words[i+2])
      
        # enter our (word1, word2):[next_words] into dictionary
        chains[key] = next_word


    print (chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)