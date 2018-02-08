from helper_dict import get_words
import random
import sys

# call helper function and get dictionary words
dictionary_words = get_words()
# returns a string
# 'a
# aa
# aaa
# aardvark
# abra'

# set dictionary words equal to arr.split

words_array = dictionary_words.split(' ')
# Returns an Array of Words
# find length of the array of words [a, aa, aaa, aardvark, abra ..., zygote]

max_index = len(words_array) - 1
# instantiate empty string of words
str_words = ""
# instantiating empty array to hold random indexes
array_random_indexes = []

# BUILDING AN ARRAY OF RANDOM INDEXES
while len(array_random_indexes) != 5:
    # instantiate new random number for index array
    rand_int = random.randint(0, max_index)

    if rand_int not in array_random_indexes:
        array_random_indexes.append(rand_int)

# FOR EVERY INDEX IN OUR ARRAY OF RANDOM INDEXES
for word_index in array_random_indexes:
    # ADD WORD TO EMPTY STRING
    str_words +=  words_array[word_index] + " "

print("random words: ", str_words)
