from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):

    def __init__(self, word_list=None):
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        # lets just shorten this to key_word
        key_word = str(word)
        i = self._index(key_word)
        # if there is no index for the word in the object
        # i.e. if the word does not exist in the object
        if i is not None:
            # if the key word is defined at index i of object
            value_of_key = self[i][1]
            # reset object with added count
            self[i] = (key_word, value_of_key + count)
            # print key_word
        else:
            # add the key word with a value pair of 1
            self.append((key_word, count))
            # increment the number of unique words in the object
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        i = self._index(word)

        if i is None:
            return 0
        else:
            return self[i][1]

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        key_word = str(word)

        if self._index(key_word) is not None:
            return True
        else:
            False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""

        # target = word to find

        index_of_word = None
        for index, tup in enumerate(self):
            if tup[0] == target:
                index_of_word = index
            # else
        return index_of_word

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
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
