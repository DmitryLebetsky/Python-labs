import re
from constants import non_declarative_check_regexp


def get_non_declarative_count(sentences_list):
    count = 0
    for sentence in sentences_list:
        if re.search(non_declarative_check_regexp, sentence):
            count = count + 1
    return count
