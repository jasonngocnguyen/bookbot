def count_book_text(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_book_characters(book_text):
    lower_characters_count = {}
    lower_characters = book_text.lower()
    for characters in lower_characters:
        if characters in lower_characters_count:
            lower_characters_count[characters] += 1
        else:
            lower_characters_count[characters] = 1
    return lower_characters_count

def sort_on(items):
    return items["num"]

def sort_dictionary(char_count):
    char_list = []
    for characters in char_count:
        count = {"char": characters, "num": char_count[characters]}
        char_list.append(count)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
