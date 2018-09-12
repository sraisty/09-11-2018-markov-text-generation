"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    # return 
    return text


def make_chains(text_string, ngram_level):
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

    # We look a the first n words in list starting at words[i], 
    for i in range(len(words) - ngram_level):
        # create our tuple that will be a key 
        key = tuple(words[i:i + ngram_level])
        # if this tuple is already in the dictionary, get its list of 
        # possible next words. 
        next_words = chains.get(key, [])
        next_words.append(words[i + ngram_level])
      
        # putkey tuple and its list of next words into dictionary
        chains[key] = next_words
    
    # print(chains)
    return chains


def make_text(chains, ngram_level):
    """Return randomly=generated text from chains."""

    words = []

    # Get our starting two words by randomly using one of the 
    # keys in our chains dictionary
    # If our choice doesn't begin with a capital letter, try again.
    while True:
        key = choice(list(chains))
        if key[0].istitle():
            # found a first word that begins with a capital letter
            break;


    # print(key)

    window = list(key)
    # print(f"window1: {window}")

    # Add the first n words, which are the key, to the return text
    words.extend(key)

    while True:
        possible_next_words = chains.get(key, None)
        if possible_next_words == None:
            break
        next_word = choice(possible_next_words)
        window.append(next_word)
        words.append(next_word)
        window.pop(0)

        key = tuple(window)
        # print(f"new key: {key}")

    return " ".join(words)




input_path = argv[1]
ngram_level = int(argv[2])


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, ngram_level)

# Produce random text
random_text = make_text(chains, ngram_level)
random_text = random_text.replace('? ', '?\n')

print(random_text)
