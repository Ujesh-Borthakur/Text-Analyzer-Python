import pytest
from cs50p_project import (
    clean_text,
    count_words,
    count_sentences,
    word_frequency,
    longest_words,
    count_syllables,
    calculate_readability,
    get_readability_label,
    estimate_reading_time,
    analyze_vocabulury,
    read_file,
)


def test_clean_text():
    assert clean_text("Hello World") == ["hello", "world"]
    assert clean_text("Hello, world! This is 'Python'.") == ["hello", "world", "this", "is", "python"]
    assert clean_text("  Extra   spaces,   here... ") == ["extra", "spaces", "here"]

def test_count_words():
    assert count_words(["hello", "world", "hello"]) == (3, 2)
    assert count_words(["this", "is", "my", "project"]) == (4, 4)
    assert count_words([]) == (0, 0)

def test_count_sentences():
    assert count_sentences("Hello world. This is my project? It is in Python!") == 3
    assert count_sentences("No... what?! Really?") == 3
    assert count_sentences("   ") == 0

def test_word_frequency():
    words = ["this", "is", "in", "python", "python", "code"]
    assert word_frequency(words, top_n=2) == [("python", 2), ("code", 1)]
    assert word_frequency(["the", "a", "is", "it"], top_n=3) == []
    assert len(word_frequency(words, top_n=1)) == 1


def test_longest_words():
    words = ["cat", "elephant", "dog", "elephant", "rhinoceros"]
    assert longest_words(words, top_n=2) == [ ("rhinoceros", 10), ("elephant", 8)]
    assert len(longest_words(words, top_n=5)) == 4
    assert longest_words([]) == []


def test_count_syllables():
    assert count_syllables("to") == 1
    assert count_syllables("like") == 1
    assert count_syllables("table") == 2


def test_calculate_readability():
    text = "The quick brown fox jumps over the lazy dog."
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert calculate_readability(text, words) == 94.3
    assert calculate_readability("", []) == 0
    assert calculate_readability("stop", ["stop"]) == 121.22


def test_get_readability_label():
    assert get_readability_label(95) == "Very Easy (upto 5th grade level)"
    assert get_readability_label(65) == "Standard (8th-9th grade level)"
    assert get_readability_label(20) == "Very Difficult (College graduate level)"


def test_estimate_reading_time():
    assert estimate_reading_time(180) == "<1 min read"
    assert estimate_reading_time(400) == "~2 min read"
    assert estimate_reading_time(700) == "~4 min read"

def test_analyze_vocabulury():
    assert analyze_vocabulury(0, 0) == (0, "Empty Text file")
    assert analyze_vocabulury(10, 8) == (80.0, "Higly Varied")
    assert analyze_vocabulury(10, 3) == (30.0, "Repetitive")

def test_read_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello Python World")

    assert read_file(str(test_file)) == "Hello Python World"

    with pytest.raises(SystemExit):
        read_file(str(tmp_path / "missing.txt"))
