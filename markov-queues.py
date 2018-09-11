"""Generate Markov text from text files."""

from random import choice


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

    for i in range(len(words) - ngram_level):
        # create our tuple that will be a key in our chain dictionary
        key = tuple(words[i:i+ngram_level])

        # if this tuple is already in the dictionary, get its list of 
        # next_words 
        next_words = chains.get(key, [])
        next_words.append(words[i+ngram_level])
        # print("key is", key, ":  value is", next_words)
      
        # enter our (word1, word2):[next_words] into dictionary
        chains[key] = next_words

    # print(chains)
    return chains


def make_text(chains, ngram_level):
    """Return text from chains."""
    words = []


    # active_words is like a "window" of n words plus the next one that we are
    # currently looking at and working on. 
    active_words_queue = []

    # Get our starting two words by randomly using one of the 
    # keys in our chains dictionary, and adding all the words in the key 
    # to our list of active_words that we are looking at
    active_words_queue.extend(choice(list(chains)))


    while True:
        key = tuple(active_words_queue[0:ngram_level])
        possible_next_words = chains.get(key, None)
        if possible_next_words == None:
            break
        active_words_queue.append(choice(possible_next_words))
        words.append(active_words_queue.pop(0))

    # If there are any active words left, the add them to list of words that
    # will be in our result string
    words.extend(active_words_queue)
    return " ".join(words)


# input_path = "green-eggs.txt"
input_path = "50-shades-of-grey.txt"
ngram_level = 5

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, ngram_level)

# Produce random text
random_text = make_text(chains, ngram_level)
random_text = random_text.replace('? ', '?\n')

print(random_text)
