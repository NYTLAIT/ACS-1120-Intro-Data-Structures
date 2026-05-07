import sys

from random import shuffle

inputs = sys.argv[1:]
shuffle(inputs)

print(' '.join(inputs))

def random_walk_second_order(chain, start_word, num_words):
    text = [start_word]
    current_word = start_word.lower().strip()

    for _ in range(num_words - 1):
        if current_word not in markov_chain:
            break
        next_words = markov_chain[current_word]
        next_word = weighted_random_word(next_words)

        text.append(next_word)
        current_word = next_word
    
    return ' '.join(text) + '.'