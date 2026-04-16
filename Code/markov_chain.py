from histogram import make_wordslist

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

if __name__ == '__main__':
    sample_text = 'I like dogs and you like dogs. I like cats but you hate cats.'
    list_words = make_wordslist(sample_text)
    print(make_markov(list_words))



