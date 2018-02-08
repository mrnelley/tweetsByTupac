from helper_dict import get_words
import random

import sys

random.seed(27)

string_of_words     = get_words()

array_of_words      = string_of_words.split(' ')

size_of_words_array = len(array_of_words) - 1

# num_words_to_pick   = random.randint(0,10)

collected_words     = ""

# 0 - num_words_to_pick
for i in range(0 , 10):
    # uniformed distribution of random int from 0 - size of words array
    random_index = int(random.uniform(0, size_of_words_array))
    collected_words += array_of_words[random_index] + ' '

print("sentence: " + collected_words)
print("number of words: 13")
