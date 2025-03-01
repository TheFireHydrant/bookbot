def get_book_words(booktext):
    with open(booktext) as f:
        text = f.read()
        words = text.split()

    return len(words)

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
    
    return chars

def sort_on(dict):
    return dict["value"]

def sort_dict(dict):
    dicts = []
    for char in dict:
        temp_dict = {"char": char, "value": dict[char]}
        dicts.append(temp_dict)
        
    dicts.sort(reverse=True, key=sort_on)

    return dicts