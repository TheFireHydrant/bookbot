from stats import get_book_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   
def main():
    print(get_book_text("books/frankenstein.txt"))
    get_book_words("books/frankenstein.txt")

main()