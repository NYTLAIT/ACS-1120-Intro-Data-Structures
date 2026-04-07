import re

def histogram(source_text):
    # Clean up words
    with open(source_text, 'r') as infile:
        text = infile.read().lower()
    words = re.split(r'\W+', text)
    print(words)

    # Build Historgram
    histogram = {}
    for word in words:
        if word and word != 1:
            histogram[word] += 1
        elif word:
            histogram[word] = 1

    return histogram

print(histogram('shackleton_quotes.txt'))

    