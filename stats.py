def count_words(txt):
    return len(txt.split())

def count_chars(txt):
    char_dict = {}
    for c in txt.lower():
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_list_dicts(d):
    list1 = []
    for c in d:
        mini_d = {}
        mini_d["char"] = c
        mini_d["num"] = d[c]
        list1.append(mini_d)
    return list1


def sort_dict(d):
    list_dicts = get_list_dicts(d)
    list_dicts.sort(reverse=True, key=sort_on)
    print(d)
