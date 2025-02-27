import sys

from stats import count_characters, count_words, sort_dictionary


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def print_sorted_dicts(dicts: list[dict[str, int]]) -> None:
    for d in dicts:
        key, value = [*d.items()][0]
        print(f"{key}: {value}")


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_content = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    num_words = count_words(book_content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    c_dict = count_characters(book_content)
    sorted_dicts = sort_dictionary(c_dict)

    print_sorted_dicts(sorted_dicts)

    print("============= END ===============")


main()
