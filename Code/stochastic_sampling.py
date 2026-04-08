import random

from histogram import histogram

def random_word(histogram):
    roll = random.randint(0, len(histogram) - 1)
    words = list(histogram)
    word = words[roll]

    print(word)
    return word

if __name__ == '__main__':
    text = 'shackleton_quote.txt'
    corpus_histogram = histogram(text)
    random_word(corpus_histogram)