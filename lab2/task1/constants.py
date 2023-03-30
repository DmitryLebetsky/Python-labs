abbreviations_regexp_list = [r'Dr\.', r'etc\.', r'i\.e\.', r'e\.g\.', r'Mr\.', r'Mrs\.', r'p\.m\.', r'a\.m\.']
dot_regexp = r'\.'

sentences_regexp = r'((?:[^.!?]+\"[^\"]+\"[,]{1}[^.]*[.]))|((?:[^.!?]+\"[^\"]+[\.!?]+\"))|([^.?!]+[.?!]+)'
non_declarative_check_regexp = r'[?!]+$'

words_regexp = r'[a-zA-Z0-9]+'
number_regexp = r'^[0-9]+$'

# ([^.?!]*(?:Dr|Mr\.)[^.?!]+[.?!]+) - with one abbreviation

