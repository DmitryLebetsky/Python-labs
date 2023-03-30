import re
from constants import NON_DECLARATIVE_REGEXP


def get_non_declarative_count(sentences_list):
    count = 0
    for sentence in sentences_list:
        if re.search(NON_DECLARATIVE_REGEXP, sentence):
            count = count + 1
    return count
