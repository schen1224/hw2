import urllib.request

from nltk.sentiment.vader import SentimentIntensityAnalyzer


# transform txt into list:
memories = open('memories.txt')
memories_list = []
for line in memories:
    memories_list.append(line.strip())
# print(memories_list)

adventures = open('adventures.txt')
adventures = []
for line in adventures:
    adventures.append(line.strip())

# Get the actual content:


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** MEMORIES OF SHERLOCK HOLMES'):
            break


def process_file(filename, skip_header):
    """
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    book = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            if word in memories_list:
                continue
            else:
                book[word] = book.get(word, 0) + 1

    return book

# Part 2 - Analysis:

# sorting all the words


def sort_words(dict):
    """
    this function sorts the dictionary in the ascending order.
    """
    sorted_values = sorted(dict.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
    return sorted_dict

# compare and contract top 10 words in both books


def top_10_words(dict):
    """
    This sort the dictionary in desceding order and return the top 10 most appeared words in the book. 
    """
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}
    sorted_top_10 = []
    for i in range(10):
        sorted_top_10.append(sorted_values[i])
    for i in sorted_top_10:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
    return sorted_dict


def compare_top_10_nonoverlapping(book_1, book_2):
    """
    (1)By evaluating top 10 most frequent words in two books, (2)this function returns the top 10 words that are not overlapping in these two books. 
    """
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key not in b2.keys():
            lt.append(key)
    for key in b2:
        if key not in b1.keys():
            lt.append(key)
    list_nonoverlapping = []
    for i in lt:
        if i not in list_nonoverlapping:
            list_nonoverlapping.append(i)
    return list_nonoverlapping


def compare_top_10_overlapping(book_1, book_2):
    """
    (1)By evaluating top 10 most frequent words in two books, (2)this function returns the top 10 words that are overlapping in these two books. 
    """
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key in b2.keys():
            lt.append(key)
    for key in b2:
        if key in b1.keys():
            lt.append(key)
    list_overlapping = []
    for i in lt:
        if i not in list_overlapping:
            list_overlapping.append(i)
    return list_overlapping

# Natural Language Processing:
