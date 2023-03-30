from check_non_declarative import get_non_declarative_count
from get_words import get_words
from replace_abbreviations import replace_abbreviations


def test_non_declarative():
    sentences_list = ["How are you?", 'He asked: "Is somebody here?"', "Hey!", "No.", "Really???", "Wow!!!"]
    expected = 4
    assert get_non_declarative_count(sentences_list) == expected


def test_get_words():
    text = 'Hey! He told: "What a beautiful 24 day today!!!" I was definitely agree with 123m4...'
    expected = ["Hey", "He", "told", "What", "a", "beautiful", "day", "today", "I", "was", "definitely", "agree",
                "with", "123m4"]
    expected_with_number = ["Hey", "He", "told", "What", "a", "beautiful", "24", "day", "today", "I", "was",
                            "definitely", "agree", "with", "123m4"]
    assert get_words(text) == expected
    assert get_words(text, False) == expected_with_number


def test_replace_abbreviations():
    text = '''Mr. Max told I need food, clothe and etc. I, Dr. Jules, answered hi,: "Mr. and Mrs. Brokers are those
    who need it, but not me." It was about 6p.m.'''
    expected = '''Mr Max told I need food, clothe and etc I, Dr Jules, answered hi,: "Mr and Mrs Brokers are those
    who need it, but not me." It was about 6pm'''
    assert replace_abbreviations(text) == expected
