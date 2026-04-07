import re

def histogram(source_text):
    # Clean up words
    with open(source_text, 'r') as infile:
        raw_text = infile.read().lower()
    words = re.split(r'\W+', raw_text)
    print(words)

    # Build Historgram
    histogram = {}
    for word in words:
        word.strip()

    return histogram

histogram('shackleton_quotes.txt')
    