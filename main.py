def main():
    book_path = ("books/frankenstein.txt")
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = char_dict_to_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    character_count = {}
    for char in book_text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count.update({char: 1})
    return character_count

def sort_on(d):
    return d["num"]

def char_dict_to_list(character_count):
    sorted_characters_list = []
    for ch in character_count:
        sorted_characters_list.append({"char": ch, "num": character_count[ch]})
    sorted_characters_list.sort(reverse=True, key=sort_on)
    return sorted_characters_list
    



main()
