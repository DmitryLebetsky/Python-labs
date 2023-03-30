from parse_text import parse_text_to_sentences
from check_non_declarative import get_non_declarative_count
from get_words import get_words
from count_n_grams import count_n_grams
from replace_abbreviations import replace_abbreviations


text_to_parse = '''
Hey! Livesey said, "The log cabin is not visible from the ship? They must be aiming at a flag. We must load a flag advance..."
Where's the map, Billy? Billy Bones. The owner of the Treasure Island map, which started it all. The "word" hey.
He drinks a lot and always has a cold. Bad character. Not married...
"The chest contains gold, diamonds, etc.", Billy said.
'''

text_to_parse = replace_abbreviations(text_to_parse)

sentences_list = parse_text_to_sentences(text_to_parse)
non_declarative_count = get_non_declarative_count(sentences_list)

words_list = get_words(text_to_parse)  # words list according to requirements (without numbers)
characters_count = sum(len(word) for word in words_list)
average_length_of_sentence = characters_count / len(sentences_list)
average_length_of_word = characters_count / len(words_list)

print()
print("Sentences count: " + str(len(sentences_list)))
print("Non-declarative sentences count: " + str(non_declarative_count))
print("Average length of sentence in characters: " + str(average_length_of_sentence))
print("Average length of word in characters: " + str(average_length_of_word))
print()

print("top-K repeated N-grams in the text:")
K = input("Enter K: ")
N = input("Enter N: ")
count_n_grams(text_to_parse, K, N)

