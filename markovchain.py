from pprint import pprint
# import numpy as np
# pac = open('corpus.txt').read()
#
# pac = pac.split()
# length = len(pac)
# # Make pairs of words
#
# def create_pairs(corpus):
#     for i in range(len(corpus) -1):
#         yield(corpus[i], corpus[i+1])
#
# pairs = create_pairs(pac)

# Here lives our dictionary of keys
# word_dictionary = {}
#
# for word1, word2 in pairs:
#     if word1 not in word_dictionary.keys():
#         word_dictionary[word1] = [word2]
#     else :
#         word_dictionary[word1].append(word2)
#
# fWord = np.random.choice(pac)
# chain = [fWord]
# numWords = 30
#
# for i in range(numWords):
#     chain.append(np.random.choice(word_dictionary[chain[-1]]))
#
# sentence = ' '.join(chain)
#
# pprint(word_dictionary)
# print sentence
# TODO: REFEACTOR FOR RUNTIME EFFICIENCY/ADD TO CORPUS/BUILD FRONT END/ADD REGEX

from dictogram import Dictogram, print_histogram

pac = open('corpus.txt').read()
pac = pac.split()

# pprint(pac)
dictogram = Dictogram(pac)
print_histogram(pac)
