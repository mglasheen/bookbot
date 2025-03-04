from stats import word_count, char_counts, list_of_char_counts, sort_on
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book = get_book_text(sys.argv[1])
    char_counts_dict = char_counts(book)
    char_counts_list = list_of_char_counts(char_counts_dict)
    introduction = f"""============ BOOKBOT ============
Analyzing book found at books/{sys.argv[1]}...
----------- Word Count ----------
Found {word_count(book)} total words
--------- Character Count -------"""
    print(introduction)
    for dict in char_counts_list:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")
    print("============= END ===============")

    

main()