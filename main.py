def main():
    """Main bookbot Func"""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    count_char = count_characters(text)
    sorted_dict = create_dict(count_char)

    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document\n")
    for i in sorted_dict:
        letter = i["letter"]
        count = i["num"]
        print(f"The '{letter}'character was found {count} times")

    print("--- End report ---")


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


def create_dict(dict) -> list:
    """turn a dictionary to a list of dictionaries."""
    new_list = []
    for key, value in dict.items():
        if key.isalpha():
            new_list.append({"letter": key, "num": value})
    return sorted(new_list, key=lambda x: x["num"], reverse=True)


if __name__ == "__main__":
    main()
