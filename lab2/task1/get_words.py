import re
from constants import words_regexp, number_regexp


def get_words(text):
    words_list = re.findall(words_regexp, text)
    # delete words containing only numbers
    words_without_numbers = [word for word in words_list if not re.search(number_regexp, word)]
    return words_without_numbers
