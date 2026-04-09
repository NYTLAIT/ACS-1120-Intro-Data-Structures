import random

from histogram import histogram

def random_word(histogram):
    roll = random.randint(0, len(histogram) - 1)
    words = list(histogram)
    word = words[roll]

    print(word)
    return word

def weighted_random_word(histogram):
    words = list(histogram)

    tokens = sum(list(histogram.values()))
    dart = random.randint(1, tokens)
    print('tokens ------', tokens)
    print('dart ------', dart)

    border = 0
    for word in words:
        border += histogram[word]
        if border >= dart:
            print('word ------', word)
            print('border ------', border)
            return word

if __name__ == '__main__':
    text = 'one fish, two fish, three fish, four fish'
    corpus_histogram = histogram(text)
    random_word(corpus_histogram)

    weighted_random_word(corpus_histogram)