import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_words
from stats import get_book_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   
def main():
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_book_words(sys.argv[1])} total words")
    print(f"--------- Character Count ---------")
    for i in sort_dict(get_book_char(sys.argv[1])):
        print(f"{i["char"]}: {i["value"]}")
    print(f"============= END ===============")
    
main()