from stats import count_words
from stats import count_characters
from stats import sort_chars_by_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    
    print("============= END ===============")
# Check if there are enough command line arguments


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main():
    # Provide the path directly here
    filepath = book_path
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_chars = sort_chars_by_count(num_characters)
    #print(f"{num_words} words found in the document")
    print_report(filepath, num_words, sorted_chars)
    

# Call main to execute your program
if __name__ == "__main__":
    main()