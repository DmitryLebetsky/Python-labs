ABBREVIATIONS_REGEXP_LIST = [r'Dr\.', r'etc\.', r'i\.e\.', r'e\.g\.', r'Mr\.', r'Mrs\.', r'p\.m\.', r'a\.m\.']
DOT_REGEXP = r'\.'

SENTENCES_REGEXP = r'((?:[^.!?]+\"[^\"]+\"[,]{1}[^.]*[.]))|((?:[^.!?]+\"[^\"]+[\.!?]+\"))|([^.?!]+[.?!]+)'
NON_DECLARATIVE_REGEXP = r'[?!]+$'

WORDS_REGEXP = r'[a-zA-Z0-9]+'
NUMBER_REGEXP = r'^[0-9]+$'
