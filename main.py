from stats import get_num_words, get_num_chars
import sys

def get_book_text(file_path):
    with open(file_path) as book:
        file_contents = book.read()
        return file_contents


def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_book_text(path)  

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_num_words(content)
    print("----------- Character Count ----------")
    get_num_chars(content)
    print("============= END ===============")



main()