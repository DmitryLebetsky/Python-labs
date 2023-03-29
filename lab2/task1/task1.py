from parse_text import parse_text_to_sentences


text_to_parse = '''
Hi! My name is Dmitry. He told: "If something happens, I am always with you.
You can trust me. I promise." I am 10 years old.
I want to be happy. Can I?! Wow, thanks!!! Are you sure????? Love you babe. Alex "If something happens, I Dr. am always
with you. You can trust me. I promise.", he told.'''

sentences_list = parse_text_to_sentences(text_to_parse)

print("Sentences count: " + str(len(sentences_list)))
