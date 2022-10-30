from thefuzz import fuzz
from thefuzz import process


def text_similarity(book1,book2):
    print(fuzz.ratio(book1,book2))

print(text_similarity('aaaa','aaahba'))
