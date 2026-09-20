# 📊 Text Analyzer

A command-line **text analysis tool built with Python** as my final project for **Harvard University's CS50P (Introduction to Programming with Python)**.

Text Analyzer reads a `.txt` file and generates a structured report containing word statistics, sentence count, readability information, vocabulary variety, frequent words, longest words, and estimated reading time.

The project focuses on applying core Python concepts such as **functions, strings, lists, sets, regular expressions, dictionaries, file handling, command-line arguments, exception handling, and automated testing with pytest**.

---

## ✨ Features

Text Analyzer provides the following analysis features:

### 📝 1. Text Cleaning

- Converts all text to lowercase.
- Removes punctuation using Python's `string.punctuation`.
- Splits the cleaned text into individual words.
- Handles extra spaces and repeated whitespace.

### 🔢 2. Word Statistics

Calculates:

- **Total words** — the total number of words found in the cleaned text.
- **Unique words** — the number of distinct words, calculated using a Python `set`.

### 📄 3. Sentence Counting

Counts sentences by splitting the original text using:

- Periods (`.`)
- Exclamation marks (`!`)
- Question marks (`?`)

Empty sentence fragments are ignored.

### 📈 4. Word Frequency

Displays the **five most frequent non-stop words** by default.

Common stop words such as `the`, `is`, `and`, `to`, and `of` are excluded so that the report focuses on more meaningful words.

The function also supports a customizable `top_n` value.

### 🏆 5. Longest Words

Finds the longest unique words in the text.

- Removes duplicate words.
- Sorts words by length in descending order.
- Displays the top three longest words by default.
- Shows the character count for each word.

### 🔤 6. Syllable Estimation

Estimates the number of syllables in a word using vowel groups.

The estimation includes a basic rule for silent ending `e`, except when the word ends in `le`.

> **Note:** This is a heuristic approach and may not correctly estimate syllables for every English word.

### 📚 7. Readability Score

Calculates a readability score using the **Flesch Reading Ease formula**:

```text
206.835
- 1.015 × (Total Words / Total Sentences)
- 84.6 × (Total Syllables / Total Words)
```

The score is rounded to two decimal places and converted into a reading-level label.

Higher scores generally indicate text that is easier to read.

### ⏱️ 8. Estimated Reading Time

Estimates reading time using an average reading speed of:

```text
200 words per minute
```

Examples:

- Fewer than 200 words → `<1 min read`
- 400 words → `~2 min read`
- 700 words → `~4 min read`

### 🧠 9. Vocabulary Variety

Calculates the **Type-Token Ratio (TTR)** as a percentage:

```text
(Unique Words / Total Words) × 100
```

The result is categorized as:

| TTR Percentage | Classification |
|---|---|
| 70% or above | Highly Varied |
| 50%–69.99% | Moderately Varied |
| Below 50% | Repetitive |

A higher TTR generally means that a larger proportion of the text consists of unique words. TTR can be affected by text length, so it should not be treated as a complete measure of writing quality.

---

## 🖥️ Example Output

```text
╔══════════════════════════════════════════════════╗
║               TEXT ANALYSIS REPORT               ║
╚══════════════════════════════════════════════════╝

 OVERVIEW
  Target File       : sample.txt
  Total Words      : 120
  Unique Words     : 86
  Total Sentences  : 8
  Estimated Read   : <1 min read

 READABILITY & VOCABULARY
  Readability Score : 82.45 / 100
  Reading Level     : Easy (6th grade level)
  Vocab Variety     : 71.67% (Higly Varied)

 MOST FREQUENT WORDS (Excluding Stop Words)
   . python           : 8 times
   . project          : 5 times
   . text             : 4 times
   . analysis         : 3 times
   . program          : 3 times

 LONGEST WORDS
   . readability      : 11 characters
   . vocabulary      : 10 characters
   . frequency       : 9 characters

════════════════════════════════════════════════════
```

> The values above are illustrative. Your actual results depend on the input text.

---

## 🗂️ Project Structure

A suggested repository structure is:

```text
Text-Analyzer/
│
├── cs50p_project.py       # Main application
├── test_cs50p_project.py # Automated tests
├── sample.txt             # Optional sample input file
├── requirements.txt       # Optional dependency list
└── README.md              # Project documentation
```

### Main Python File

`cs50p_project.py` contains:

| Function | Purpose |
|---|---|
| `clean_text()` | Converts text to lowercase, removes punctuation, and returns words |
| `count_words()` | Calculates total and unique word counts |
| `count_sentences()` | Estimates the number of sentences |
| `word_frequency()` | Returns the most frequent non-stop words |
| `longest_words()` | Returns the longest unique words |
| `count_syllables()` | Estimates syllables in a word |
| `calculate_readability()` | Calculates the Flesch Reading Ease score |
| `get_readability_label()` | Converts the score into a reading-level label |
| `estimate_reading_time()` | Estimates reading time at 200 words per minute |
| `analyze_vocabulury()` | Calculates vocabulary variety using TTR |
| `read_file()` | Reads the input file and handles missing files |
| `main()` | Coordinates the complete analysis and prints the report |

---

## ⚙️ Requirements

- **Python 3.8 or later** recommended
- `pytest` for running automated tests
- A plain-text file with a `.txt` extension, or another readable text file

The main application uses Python standard-library modules:

```python
import string
import re
import sys
from collections import Counter
```

No external package is required to run the main analyzer itself.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd Text-Analyzer
```

Replace the repository URL with the actual URL of your GitHub repository.

### 2. Check Python Installation

```bash
python --version
```

Depending on your operating system, you may need to use:

```bash
python3 --version
```

### 3. Install pytest

```bash
pip install pytest
```

Or:

```bash
python -m pip install pytest
```

---

## ▶️ How to Run the Program

The program accepts the path of a text file through a command-line argument.

### Basic Command

```bash
python cs50p_project.py <filepath>
```

### Example

```bash
python cs50p_project.py sample.txt
```

You can also provide a file path from another directory:

```bash
python cs50p_project.py "documents/article.txt"
```

### Incorrect Usage

If no file path or more than one argument is provided, the program displays:

```text
Usage: python cs50p_project.py <filepath>
```

### Missing File

If the specified file does not exist, the program displays an error message and exits:

```text
Error: The file sample.txt was not found
```

---

## 🧪 Testing

The project includes automated tests written with **pytest**.

The test suite checks the behavior of the individual functions instead of testing only the complete program.

### Test Coverage

The tests cover:

- Text cleaning and punctuation removal
- Word counting
- Sentence counting
- Stop-word filtering and frequency calculation
- Longest-word extraction
- Syllable estimation
- Readability-score calculation
- Reading-level labels
- Reading-time estimation
- Vocabulary-variety classification
- Successful file reading
- Missing-file handling and `SystemExit`

### Run All Tests

If the test file is named `test_cs50p_project.py`, run:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

### Run a Specific Test

```bash
pytest -v test_cs50p_project.py::test_clean_text
```

### Test Design

The test suite uses:

- `assert` statements to verify expected results.
- `tmp_path` to create temporary test files.
- `pytest.raises(SystemExit)` to verify that missing files are handled correctly.

The tests help ensure that the program behaves as expected and make future changes safer.

---

## 🧩 Concepts Demonstrated

This project applies several important Python programming concepts:

### Functions

The program is divided into small, focused functions. This improves readability, maintainability, and testing.

### Strings

String methods are used for:

- Lowercase conversion
- Whitespace handling
- Punctuation removal
- Suffix checking

### Lists

Lists store cleaned words, filtered words, and analysis results.

### Sets

Sets are used to identify unique words and remove duplicates when finding the longest words.

### Dictionaries and Counter

`collections.Counter` is used to count word occurrences efficiently.

### Regular Expressions

The `re` module is used to:

- Split sentences based on punctuation.
- Identify groups of vowels for syllable estimation.

### File Handling

The program uses `open()` and a `with` statement to safely read text files.

### Exception Handling

`FileNotFoundError` is handled to provide a user-friendly error message when a file cannot be found.

### Command-Line Arguments

`sys.argv` is used to accept the input file path from the terminal.

### Testing

`pytest` is used to automate validation of the program's functions.

---

## 🧮 Algorithms and Formulas

### Type-Token Ratio

```text
TTR = (Number of Unique Words / Total Number of Words) × 100
```

TTR is useful for describing vocabulary diversity, but the value can vary considerably depending on text length.

### Flesch Reading Ease

```text
Score = 206.835
        - 1.015 × (Words / Sentences)
        - 84.6 × (Syllables / Words)
```

General interpretation used by this project:

| Score Range | Reading Label |
|---|---|
| 90 and above | Very Easy |
| 80–89.99 | Easy |
| 70–79.99 | Fairly Easy |
| 60–69.99 | Standard |
| 50–59.99 | Fairly Difficult |
| 30–49.99 | Difficult |
| Below 30 | Very Difficult |

The reading-level labels are approximate and are intended for general interpretation rather than formal academic assessment.

---

## ⚠️ Limitations

This project is designed as a practical educational text-analysis tool. It uses simple heuristics, so its results have limitations.

### Text Cleaning

- Punctuation is removed using `string.punctuation`.
- Apostrophes are removed rather than preserving contractions.
- The analyzer is primarily designed for English-like text.
- Hyphenated words may be split into separate words.

### Sentence Counting

- Sentence boundaries are identified using `.`, `!`, and `?`.
- Abbreviations such as `Dr.` or `etc.` may cause inaccurate counts.
- Decimal numbers and unusual punctuation patterns may affect the result.

### Syllable Estimation

- Syllables are estimated using vowel groups.
- English pronunciation contains many exceptions.
- The algorithm may overestimate or underestimate syllables in certain words.

### Readability

- The Flesch Reading Ease formula is most appropriate for English prose.
- The result depends on the accuracy of sentence and syllable counts.
- A numerical score cannot fully represent writing quality, meaning, or complexity.

### Vocabulary Variety

- TTR is influenced by the length of the text.
- Short texts may appear highly varied even when they are not representative.
- The classification is a simple interpretation rather than a definitive language-quality assessment.

### Reading Time

- Reading speed is fixed at 200 words per minute.
- Individual reading speeds vary based on familiarity, difficulty, and reading purpose.

---

## 🔮 Possible Future Improvements

Potential improvements for future versions include:

- [ ] Support for multiple input files.
- [ ] Export reports to `.txt`, `.csv`, or `.json`.
- [ ] Add command-line options using `argparse`.
- [ ] Improve sentence detection using more advanced natural-language processing.
- [ ] Improve syllable estimation with a pronunciation dictionary.
- [ ] Add support for additional languages.
- [ ] Display word-frequency charts.
- [ ] Add stop-word customization through a configuration file.
- [ ] Add unit tests for more edge cases.
- [ ] Build a graphical user interface or web interface.
- [ ] Add a word cloud visualization.
- [ ] Include a configurable reading-speed setting.

---

## 🎓 CS50P Project Context

This project was developed as my **final project for CS50P: Introduction to Programming with Python**.

The purpose of the project was to combine the programming concepts learned throughout the course into a practical application.

Through this project, I practiced:

- Designing a program using reusable functions.
- Processing and analyzing text data.
- Working with files and command-line inputs.
- Handling errors gracefully.
- Using Python's built-in modules.
- Writing automated tests with pytest.
- Structuring a project for public documentation and version control.

---

## 📌 Usage Summary

```bash
# Run the analyzer
python cs50p_project.py sample.txt

# Run the complete test suite
pytest

# Run tests with detailed output
pytest -v
```

---

## ⭐ Acknowledgements

- **Harvard CS50P** — for the course concepts and project-based learning experience.

---
