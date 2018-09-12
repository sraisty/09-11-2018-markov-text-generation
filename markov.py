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


def make_chains(chains, text_string, ngram_level):
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


    # Add the first n words, which are the key, to the return text
    words.extend(key)


    while True:
        # With our key, get the possible next words and then pick one at random
        possible_next_words = chains.get(key, None)
        if possible_next_words == None:
            break
        next_word = choice(possible_next_words)

        # Add the selected next_word to our output text
        words.append(next_word)

        # Now, look at the next set of words. Change our key to be the last
        # n words in our wordlist, and do the loop again
        key = tuple(words[-ngram_level:])



    # To make sure our text ends with a complete sentence:
    # from end of list, look for the last word that has sentence-ending 
    # punctuation. If it doesn't, chop that word from the list.
    while True:
        last_char = words[-1][-1]
        if last_char in ['.', '?', '!']:
            break;
        else:    
            words.pop()

    # Make string out of all the words in the list with spaces in between
    return " ".join(words)





filenames = argv[2:]
ngram_level = int(argv[1])

# Open each file and add it to the chains dictionary
chains = {}

for input_file in filenames:    
    input_text = open_and_read_file(input_file)

    # Get a Markov chain
    chains = make_chains(chains, input_text, ngram_level)

# Produce random text
random_text = make_text(chains, ngram_level)
random_text = random_text.replace('? ', '?\n')

print(random_text)
