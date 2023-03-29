sentences_regexp = r'(?:Dr\.)(SKIP)(F)|((?:[^.]+\"[^\"]+\"[,]{1}[^.]*[.]))|((?:[^.]+\"[^\"]+\"))|([^.?!]+[.?!]+)'
non_declarative_check_regexp = r'[?!]+$'

words_regexp = r'[a-zA-Z0-9]+'
number_regexp = r'^[0-9]+$'

# ([^.?!]*(?:Dr|Mr\.)[^.?!]+[.?!]+) - with one abbreviation

