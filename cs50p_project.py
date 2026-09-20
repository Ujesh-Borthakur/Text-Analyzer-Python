import string
import re
import sys
from collections import Counter

def clean_text(text):

    lower_text = text.lower()
    no_punct = lower_text.translate(str.maketrans('', '', string.punctuation))

    return no_punct.split()

def count_words(words):
    total_words = len(words)
    unique_words = len(set(words))

    return total_words, unique_words

def count_sentences(text):

    if not text.strip():
        return 0

    sentences = re.split(r'[.!?]+', text)

    valid_sentences = [s for s in sentences if s.strip()]

    return max(1, len(valid_sentences))

def word_frequency(words, top_n: int = 5):

    stop_words= {"a", "an", "the", "and", "but", "or", "for", "nor", "so", "yet",
    "in", "on", "at", "by", "to", "of", "with", "is", "it", "this", "that" }

    filtered_words = [word for word in words if word not in stop_words]

    counts = Counter(filtered_words)

    return counts.most_common(top_n)

def longest_words(words, top_n: int = 3):
    unique_words=set(words)

    sorted_words=sorted(unique_words, key=len, reverse=True)

    return [(word, len(word)) for word in sorted_words[:top_n]]

def count_syllables(words):

    word=words.lower()

    if len(words)<3:
        return 1
    vowel_group=re.findall(r'[aeiouy]+', word)
    count=len(vowel_group)

    if word.endswith('e') and not word.endswith('le') and count > 1:
        count-=1

    return max(1, count)

def calculate_readability(text, words):
    if not words:
        return 0

    total_sentences=count_sentences(text)
    total_words=len(words)

    total_syllables=sum(count_syllables(word) for word in words)

    score = ( 206.835 -1.015 * (total_words/total_sentences) -84.6 * (total_syllables/total_words))

    return round(score,2)

def get_readability_label(score):
    
    if score >= 90:
        return "Very Easy (upto 5th grade level)"
    elif score >= 80:
        return "Easy (6th grade level)"
    elif score >= 70:
        return "Fairly Easy (7th grade level)"
    elif score >= 60:
        return "Standard (8th-9th grade level)"
    elif score >= 50:
        return "Fairly Difficult (10th-12th grade level)"
    elif score >= 30:
        return "Difficult (College level)"
    else:
        return "Very Difficult (College graduate level)"

def estimate_reading_time(total_words):
    words_per_minute=200
    if total_words< words_per_minute:
        return "<1 min read"
    minutes=round(total_words/words_per_minute)
    return f"~{minutes} min read"

def analyze_vocabulury(total_words, unique_words):
    if total_words==0:
        return 0, "Empty Text file"
    TTR_percentage=round((unique_words/total_words)*100, 2)
    if TTR_percentage >= 70.0:
        label="Higly Varied"
    elif TTR_percentage >=50.0:
        label="Moderately Varied"
    else:
        label="Repetitive"

    return TTR_percentage, label

def read_file(filepath: str):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found")
        sys.exit(1)

def main():

    if len(sys.argv)!=2:
        print("Usage: python cs50p_project.py <filepath>")
        sys.exit(1)

    filepath=sys.argv[1]

    raw_text=read_file(filepath)

    words=clean_text(raw_text)

    total_words, unique_words=count_words(words)
    total_sentences=count_sentences(raw_text)
    readability_score=calculate_readability(raw_text, words)
    readability_label=get_readability_label(readability_score)
    reading_time = estimate_reading_time(total_words)
    top_words=word_frequency(words, top_n=5)
    longest=longest_words(words, top_n=3)
    vocab_var, vocab_label = analyze_vocabulury(total_words, unique_words)

    print("╔══════════════════════════════════════════════════╗")
    print("║               TEXT ANALYSIS REPORT               ║")
    print("╚══════════════════════════════════════════════════╝")
    
    print("\n OVERVIEW")
    print(f"  {'Target File':<18}: {filepath}")
    print(f"  {'Total Words':<18}: {total_words}")
    print(f"  {'Unique Words':<18}: {unique_words}")
    print(f"  {'Total Sentences':<18}: {total_sentences}")
    print(f"  {'Estimated Read':<18}: {reading_time}")

    print("\n READABILITY & VOCABULARY")
    print(f"  {'Readability Score':<18}: {readability_score} / 100")
    print(f"  {'Reading Level':<18}: {readability_label}")
    print(f"  {'Vocab Variety':<18}: {vocab_var}% ({vocab_label})")

    print("\n MOST FREQUENT WORDS (Excluding Stop Words)")
    if top_words:
        for word, count in top_words:
            print(f"   . {word:<16} : {count} times")
    else:
        print("   . No non-stop words found.")

    print("\n LONGEST WORDS")
    if longest:
        for word, length in longest:
            print(f"   . {word:<16} : {length} characters")
    else:
        print("   . No words found.")

    print("\n" + "═" * 52)


if __name__ == "__main__":
    main()
