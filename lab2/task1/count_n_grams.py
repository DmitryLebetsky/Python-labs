from parse_text import parse_text_to_sentences
from get_words import get_words


def count_n_grams(text, k, n):  # top-K repeated N-grams
    if not k.isnumeric() or not n.isnumeric():
        print("Entered values are incorrect!")
        return
    k = int(k)
    n = int(n)

    n_grams_dict = dict()
    sentences_list = parse_text_to_sentences(text)

    # find n-grams and their count in text
    for sentence in sentences_list:
        words_from_sentence = get_words(sentence, False)
        start_index = 0
        end_index = start_index + n
        while end_index <= len(words_from_sentence):
            n_gram = ' '.join(words_from_sentence[start_index:end_index])
            if n_gram in n_grams_dict:
                n_grams_dict[n_gram] = n_grams_dict[n_gram] + 1
            else:
                n_grams_dict[n_gram] = 1
            start_index += 1
            end_index += 1

    sorted_n_grams_dict = dict(sorted(n_grams_dict.items(), key=lambda x: x[1], reverse=True))

    top_k_n_grams_dict = dict(list(sorted_n_grams_dict.items())[0:k])

    for n_gram in top_k_n_grams_dict:
        print(str(n_gram) + " - " + str(top_k_n_grams_dict[n_gram]))
