"""
find first non repeating char in string
"""


def find_first_non_repeating_char(input):
    input_str_map = {}
    for ch in input:
        if ch in input_str_map:
            input_str_map[ch] += 1
        else:
            input_str_map[ch] = 1

    for item_key, value in input_str_map.items():
        if value == 1:
            return item_key

print(find_first_non_repeating_char("aabbffgghoo"))