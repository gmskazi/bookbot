def main():
    """Main bookbot Func"""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    print(f"{number_of_words} words found in the document")
    print(count_characters(text))


def get_book_text(path) -> str:
    """Return the book text."""
    with open(path) as f:
        return f.read()


def get_num_words(words) -> int:
    """Return the number of words."""
    words = words.split()
    return len(words)


def count_characters(texts) -> dict:
    """Count the number of characters appear in the string."""
    letters = {}
    lowered_string = texts.lower()
    for letter in lowered_string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


if __name__ == "__main__":
    main()
