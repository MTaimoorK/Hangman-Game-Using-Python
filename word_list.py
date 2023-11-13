import nltk
import random

nltk.download('words')
# Get a list of English words
word_list = nltk.corpus.words.words()
random_words = random.sample(word_list, 100)