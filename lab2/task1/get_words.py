import re
from constants import WORDS_REGEXP, NUMBER_REGEXP


def get_words(text, delete_numbers=True):
    words_list = re.findall(WORDS_REGEXP, text)
    # delete words containing only numbers
    if delete_numbers:
        words_without_numbers = [word for word in words_list if not re.search(NUMBER_REGEXP, word)]
        return words_without_numbers
    else:
        return words_list
