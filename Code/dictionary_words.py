import sys
from random import sample

num_of_words = int(sys.argv[1])

with open('/usr/share/dict/words', 'r') as infile:
    all_words = infile.readlines()

chosen_words = sample(all_words, k=num_of_words)
stripped_words = [word.strip() for word in chosen_words]

print(stripped_words[0].capitalize() + ' ' + ' '.join(stripped_words[1:]) + '.')
    