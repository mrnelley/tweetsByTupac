from __future__ import division, print_function  # Python 2 and 3 compatibility
from pprint import pprint

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Define key as string instance of each word passed into dictionary
        key_word_in_dictionary = str(word)
        # Value is the number of found instances of a key otherwise none because
        # key word is not in dictionary object
        unlocked_value = self.get(key_word_in_dictionary, None)
        # If there is no instance of this word in dictionary, add to dictionary
        # and increment number of distinct words in dictionary total (self.types)
        if unlocked_value is None:
            self[key_word_in_dictionary] = count
            self.types += 1
        # else just add 1 to unlocked number value of instances of key in dictionary
        else:
            self[key_word_in_dictionary] = unlocked_value + count
        # increment number of total words in dictionary
        self.tokens += count


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # self.get(key) return value of key
        key_word_in_dictionary = str(word)
        unlocked_value = self.get(key_word_in_dictionary, None)
        if unlocked_value is None:
            return 0
        else:
            return unlocked_value
        # that was easy

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # pprint(word_list)
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: ')
    pprint(histogram)
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-4:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()

def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
