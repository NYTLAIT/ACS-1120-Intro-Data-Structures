import re

def histogram(source_text):
    # Obtain corpus
    try: 
        with open(source_text, 'r') as infile:
            raw_text = infile.read()
    except:
        try:
            if type(source_text) == str:
                raw_text = source_text
        except:
            return print('Invalid text - Accepts only string and txt')

    # Grab individual words
    split_words = re.split(r"[^\w+']", raw_text)
    print('Split up words ------', split_words, '\n')
    # Clean up words
    words = [word.lower() for word in split_words if word]
    print('Clean up words ------', words, '\n')

    # Build Historgram
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1

    # Return histogram
    return histogram


def unique_words(histogram):
    return len(histogram)

def frequency(given_word, histogram):
    word = given_word.strip().lower()
    return histogram.get(word, 0)

if __name__ == '__main__':
    text = 'shackleton_quote.txt'
    text_histogram = histogram(text)
    given_word = "That's"
    print('histogram ------', text_histogram)
    print('unique_words -------', unique_words(text_histogram))
    print('frequency -------', f'{given_word}: {frequency(given_word, text_histogram)}')

# Known Issues: 
# 1. Takes txt and not string; no safeguard 
# 2. Apostrophes that are not to extend words can cause issues


# TODO:
# 1. Make documentations(doc strings)