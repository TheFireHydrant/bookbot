def get_book_words(booktext):
    with open(booktext) as f:
        text = f.read()
        words = text.split()
    print(f"{len(words)} words found in the document")