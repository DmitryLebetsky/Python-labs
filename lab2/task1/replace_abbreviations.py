import re
from constants import ABBREVIATIONS_REGEXP_LIST, DOT_REGEXP


def replace_abbreviations(text):
    for abbr_regexp in ABBREVIATIONS_REGEXP_LIST:
        replacement = abbr_regexp.replace(DOT_REGEXP, '')
        text = re.sub(abbr_regexp, replacement, text)

    return text
