import re

def histogram(source_text):
    # Clean up words
    with open(source_text, 'r') as infile:
        raw_text = infile.read()

    split_words = re.split(r"[^\w+']", raw_text)
    print('Split up words ------', split_words, '\n')

    words = [word.lower() for word in split_words if word]
    print('Cleaned up words ------', words, '\n')

    # Build Historgram
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    return histogram


def unique_words(histogram):
    return len(histogram)

def frequency(given_word, histogram):
    word = given_word.strip().lower()
    if histogram[word]:
        return histogram[word]
    else:
        return 0

if __name__ == '__main__':
    text = 'shackleton_quotes.txt'
    text_histogram = histogram(text)
    print('histogram ------', text_histogram)
    print('unique_words -------', unique_words(text_histogram))
    print('frequency -------', frequency('I', text_histogram))