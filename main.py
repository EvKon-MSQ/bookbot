def main():
    book_path = ("books/frankenstein.txt")
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(word_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

main()
