import re

def histogram(source_text):
    """
    Generate a frequency histogram via dictionary from a txt file or string
    
    Args:
        source_text (str, .txt): body of text to be represented as the histogram
    Returns:
        ditionary: a frequency histogram - keys are the words and their value are their frequency
    """
    # Obtain corpus
    raw_text = None
    try: 
        with open(source_text, 'r') as infile:
            raw_text = infile.read()
    except:
        if isinstance(source_text, str):
            raw_text = source_text
        else:
            print('Invalid text - Accepts only string and txt')
            return

    # Grab individual words
    split_words = re.split(r"[^\w']+", raw_text)
            # print('Split up words ------', split_words, '\n')
    # Clean up words
    words = [word.lower() for word in split_words if word]
            # print('Clean up words ------', words, '\n')

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
    # Testing txt
    print('\n')
    txt_text = 'shackleton_quote.txt'
    txt_text_histogram = histogram(txt_text)
    txt_given_word = "That's"
    print('(txt)histogram ------', txt_text_histogram)
    print('(txt)unique_words -------', unique_words(txt_text_histogram))
    print('(txt)frequency -------', f'{txt_given_word}: {frequency(txt_given_word, txt_text_histogram)}')
    # Testing str
    print('\n')
    str_text = 'For scientific discovery give me Scott; for speed and efficiency ' \
        'of travel give me Amundsen; but when disaster strikes and all hope is gone, ' \
        'get down on your knees and pray for Shackleton.'
    str_text_histogram = histogram(str_text)
    str_given_word = 'for'
    print('(str)histogram ------', str_text_histogram)
    print('(str)unique_words -------', unique_words(str_text_histogram))
    print('(str)frequency -------', f'{str_given_word}: {frequency(str_given_word, str_text_histogram)}')
    # Testing error handling
    print('\n')
    error_text = 404
    error_text_histogram = histogram(error_text)
    

# Known Issues: 
# 2. Apostrophes that are not to extend words will cause issues


# TODO:
# 1. Make documentations(doc strings)