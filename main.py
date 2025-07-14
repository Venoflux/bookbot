import sys
from stats import get_book_word_count
from stats import get_book_letter_count
from stats import sort_book_letter_count


def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return filecontents


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif sys.argv[1]:
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")

        print("----------- Word Count ----------")
        print(f"Found {get_book_word_count(get_book_text(path))} total words")

        print("--------- Character Count -------")
        count_list = get_book_letter_count(get_book_text(path))
        sort_book_letter_count(count_list)

        for character in count_list:
            print(f"{character['char']}: {character['num']}")

        print("============= END ===============")


if __name__ == "__main__":
    main()
