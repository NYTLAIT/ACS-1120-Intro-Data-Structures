from histogram import make_wordslist
from stochastic_sampling import weighted_random_word
import random

def make_markov(list_words):
    chain = {}
    for state in range(len(list_words) - 1):
        current_word = list_words[state]
        next_word = list_words[state + 1]

        if current_word not in chain:
            chain[current_word] = {}
        if next_word not in chain[current_word]:
            chain[current_word][next_word] = 0

        chain[current_word][next_word] += 1
    return chain

def random_walk(markov_chain, start_word, num_words):
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
    
if __name__ == '__main__':
    sample_text = 'I like dogs and you like dogs. I like cats but you hate cats.'
    list_words = make_wordslist(sample_text)
    chain = make_markov(list_words)
    print(chain)
    walk = random_walk(chain, 'I', 16)
    print(walk)



