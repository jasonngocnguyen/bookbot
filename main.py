import sys
from stats import *

def main():
    #book_path = "books/frankenstein.txt"

    #print("Book Path:", sys.argv[1])
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        total_count = count_book_text(book_text)
        total_character_count = count_book_characters(book_text)
        sorted_character_count = sort_dictionary(total_character_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {total_count} total words")
        print("--------- Character Count -------")
        for entry in sorted_character_count:
            if not entry["char"].isalpha():
                continue
            print(f"{entry['char']}: {entry['num']}")

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

main()