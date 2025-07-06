import sys
from stats import *


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(filepath):
    txt = get_book_text(filepath)
    word_count = count_words(txt)
    char_dict = count_chars(txt)
    sorted_dict = get_list_dicts(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}.")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for elem in sorted_dict:
        if elem["char"].isalpha():
            print(str(elem["char"]) + ": " + str(elem["num"]))
    
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print_report(sys.argv[1])

main()