import timeit

from dictogram import Dictogram
from listogram import Listogram
from hashtablogram import HashTablogram

words_100 = [f'word{i}' for i in range(100)]
words_10000 = [f'word{i}' for i in range(10000)]

dictogram_100 = Dictogram(words_100)
dictogram_1000 = Dictogram(words_10000)

listogram_100 = Listogram(words_100)
listogram_1000 = Listogram(words_10000)

hashtablogram_100 = HashTablogram(words_100)
hashtablogram_1000 = HashTablogram(words_10000)



# TEST BIG
iterations = 10000

dict_time = timeit.timeit(
    lambda: dictogram_1000.frequency('word9999'),
    number=iterations
)

list_time = timeit.timeit(
    lambda: listogram_1000.frequency('word9999'),
    number=iterations
)

hash_time = timeit.timeit(
    lambda: hashtablogram_1000.frequency('word9999'),
    number=iterations
)

print("Dictogram:", dict_time)
print("Listogram:", list_time)
print("Hashtablogram:", hash_time)