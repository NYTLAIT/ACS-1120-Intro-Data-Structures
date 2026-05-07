from hashtable import HashTable

class HashTablogram(HashTable):
    def __init__(self, word_list):
        super(HashTablogram, self).__init__()

        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram

        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self.tokens += count
        if self.contains(word):
            current_count = self.get(word)
            self.set(word, current_count + count)
        else:
            self.set(word, count)
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if self.contains(word):
            return self.get(word)
        return 0