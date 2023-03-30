import re
from constants import SENTENCES_REGEXP


def parse_text_to_sentences(text):
    sentences_iterator = re.finditer(SENTENCES_REGEXP, text, re.MULTILINE)
    sentences_list = [sentence.group() for sentence in sentences_iterator]
    return sentences_list
