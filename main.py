import sys
from stats import count_words_in_book
from stats import print_char_report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

word_count = count_words_in_book(book_path)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
print_char_report(book_path)
print("============= END ===============")
