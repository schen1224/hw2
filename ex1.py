import random
import string
import sys
from unicodedata import category
from thefuzz import fuzz

# Part 1: Cleaning file

def process_file(filename, skip_header):
    """
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    book = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            book[word] = book.get(word, 0) + 1

    return book


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

# Part 2: Analyzing the Text

def total_words(book):
    """Returns the total of the frequencies in a histogram."""
    return sum(book.values())

def most_common(book, excluding_stopwords=True):
    """
    Makes a list of word-freq pairs(tuples) in descending order of frequency.
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('data/stopwords.txt', False)

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in book.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t

def top_10_words(book):
    """
   This sort the dictionary in desceding order and return the top 10 most appeared words in the book.
    """
    t = most_common(book)
    result={}
    for freq, word in t[:10]:
        result[word]=freq
    return result


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

# Part 3: Natural Language Processing

# Part 4: Text Similarity
def text_similarity(book1,book2):
    print(fuzz.ratio(book1,book2))

# Part 5: Text Clustering
def main():
    adv = process_file('adventures.txt', skip_header=True)
    ret= process_file('The Return of Sherlock Holmes.txt', skip_header=True)

    # print(f'The total words in Adventures are {total_words(adv)}')
    # print(f'The total words in The Return of Sherlock Holmes are {total_words(ret)}')
    # print(f'The top 10 words in Adventures are:{top_10_words(adv)}')
    # print(f'The top 10 words in The Return of Sherlock Holmes are:{top_10_words(ret)}')
    # print(f'The non overlapping words in the top 10 common words in two books are:{compare_top_10_nonoverlapping(adv, ret)}')
    # print(f'The overlapping words in the top 10 common words in two books are:{compare_top_10_overlapping(adv, ret)}')

    print(f'The text similarity based in the fuzz ratio is {text_similarity(adv,ret)}%')






if __name__ == '__main__':
    main()