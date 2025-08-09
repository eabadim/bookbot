def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words_in_book(path_to_file):
    word_list = get_book_text(path_to_file).split()
    word_count = len(word_list)
    return word_count

def char_count_dict(path_to_file):
    lowercase_text = get_book_text(path_to_file).lower()
    dict = {}
    for character in lowercase_text:
        if character.isalpha():
            if character in dict:
               dict[character] += 1
            else:
                dict[character] = 1
    return dict

def create_new_pairs(path_to_file):
    old_pairs = char_count_dict(path_to_file)
    new_pairs = []
    for i in old_pairs.items():
        new_pairs.append({"char": i[0],"num": i[1]})
    return new_pairs

def sort_on(items):
    return items["num"]

def sort_pairs(path_to_file):
    new_pairs = create_new_pairs(path_to_file)
    new_pairs.sort(reverse=True, key=sort_on)
    return new_pairs

def print_char_report(path_to_file):
    char_count_list = sort_pairs(path_to_file)
    for i in char_count_list:
        print(f"{i['char']}: {i['num']}")
    return char_count_list

