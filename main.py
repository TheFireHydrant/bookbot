
from stats import get_book_words
from stats import get_book_char
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   
def main():
    filepath = "books/frankenstein.txt"
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_book_words(filepath)} total words")
    print(f"--------- Character Count ---------")
    for i in sort_dict(get_book_char(filepath)):
        print(f"{i["char"]}: {i["value"]}")
    print(f"============= END ===============")

main()