from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def print_report(file_path, word_count, char_count):
    print(f'''============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------''')
    for char in char_count:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["count"]}')
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_char_count = sort_count_chars(char_count)
    print_report(file_path, word_count, sorted_char_count)
main()
