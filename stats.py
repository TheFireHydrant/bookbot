def get_book_words(booktext):
    with open(booktext) as f:
        text = f.read()
        words = text.split()
    print(f"{len(words)} words found in the document")

def get_book_char(booktext):
    with open(booktext) as f:
        chars = {}
        text = f.read()
        lower_text = text.lower()
        for char in range(len(lower_text)):
            if lower_text[char] not in chars:
                chars[(lower_text[char])] = 1
            else:
                chars[(lower_text[char])] += 1

    print(chars)
