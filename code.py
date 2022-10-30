import urllib.request
import string


# # transform txt into list:
# memories = open('memories.txt')
# memories_list = []
# for line in memories:
#     memories_list.append(line.strip())
# # print(memories_list)

# adventures = open('adventures.txt')
# adventures = []
# for line in adventures:
#     adventures.append(line.strip())

stop_words = open('stopwords.txt')
stop_words_list = []
for line in stop_words:
    stop_words_list.append(line.strip())

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

            if word in stop_words_list:
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

def main():
    # please keep the following four lines of code UN-commented when running the main function
    adv = process_file('adventures.txt', skip_header=True)
    memo = process_file('memories.txt', skip_header=True)
    # nltk_Smith = open('An Inquiry into the Nature and Causes of the Wealth of Nations.txt', 'r', encoding='utf-8').read()
    # nltk_Hamilton = open('The Federalist Papers.txt', 'r', encoding='utf-8').read()


    print(f'top ten words appeared in Adventures : {top_10_words(adv)}')
    print(f'top ten words appeared in memories: {top_10_words(memo)}')

    # print(f'The difference between Smith\'s book and Hamilton\'s book is: {compare_top_10(book_Smith, book_Hamilton)}')

    # print(f'The Score for sentiment analysis for Smith\'s book is {sentiment_analysis(nltk_Smith)}')
    # print(f'The Score for sentiment analysis for Hamilton\'s book is {sentiment_analysis(nltk_Hamilton)}')

    # print(f'The difference in score between Smith\'s book and Hamilton\'s book is {compare_sentiment_analysis(nltk_Smith, nltk_Hamilton)}')

    # print(plot(nltk_Smith))
    # plt.savefig('Smith.png')

    # print(plot(nltk_Hamilton))
    # plt.savefig('Hamilton.png')

    print(f'The Jaccard Similarity Score between the two books is {jaccard_similarity(nltk_Smith, nltk_Hamilton): 0.5f}')

if __name__ == "__main__":
    main()
