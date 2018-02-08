# Open dictionary
def get_words():
    with open('./corpus.txt') as dictionary_file:
        # read words
        # instantiate new variable to contain word list
        dictionary_words = dictionary_file.read()
    # return words
    return dictionary_words
