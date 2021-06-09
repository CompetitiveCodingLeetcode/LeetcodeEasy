"""
remove the specified characters from a given string which are specified in another string
"""


def remove_one_str_from_another(replace_str, target_str):
    replace_char_map = {}
    new_str = ''
    for ch in replace_str:
        if ch not in replace_char_map:
            replace_char_map[ch] = 1
    for ch in target_str:
        if ch not in replace_char_map:
            new_str += ch
    return new_str


print(remove_one_str_from_another("abc", "addklckbnb"))
