def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def count_book_text():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words = book_text.split()
    word_count = len(words)
    return word_count



def main():
    total_count = count_book_text()
    print(f"Found {total_count} total words")

main()