def word_count(text):
    words = text.split()
    return len(words)

def char_counts(text):
    char_counts_dict = {}
    for char in text:
        if char.lower() in char_counts_dict:
            char_counts_dict[char.lower()] += 1
        else:
            char_counts_dict[char.lower()] = 1
    return char_counts_dict

def sort_on(dict):
    return dict["num"]

def list_of_char_counts(dict):
    char_counts_list = []
    for char in dict:
        char_counts_list.append({"name": char, "num": dict[char]})
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list
    