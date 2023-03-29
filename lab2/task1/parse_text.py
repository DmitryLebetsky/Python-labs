import re
from constants import sentences_regexp


def parse_text_to_sentences(text):
    sentences_iterator = re.finditer(sentences_regexp, text, re.MULTILINE)
    sentences_list = [sentence.group() for sentence in sentences_iterator]
    return sentences_list
