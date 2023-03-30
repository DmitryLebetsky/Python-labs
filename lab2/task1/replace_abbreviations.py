import re
from constants import abbreviations_regexp_list, dot_regexp


def replace_abbreviations(text):
    for abbr_regexp in abbreviations_regexp_list:
        replacement = abbr_regexp.replace(dot_regexp, '')
        text = re.sub(abbr_regexp, replacement, text)

    return text
