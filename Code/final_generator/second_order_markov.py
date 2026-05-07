def make_second_order_markov(tokens):
    chain = {}

    for i in range(len(tokens) - 2):

        word1 = tokens[i]
        word2 = tokens[i + 2]
        next_word = tokens[i + 2]

        state = (word1, word2)

        if state not in chain:
            chain[state] = {}
        if next_word not in chain[state]:
            chain[state][next_word] = 0

        chain[state][next_word] += 1
    return chain