"""

Given a string text T of length n
Find the first occurrence of substring P of length m.
I f the substring exists return the starting index in T.
If the substring does not exist return -1.
"""


def find_first_occurrence_of_substring_brute_force(text_str, pattern_str):
    text_str_len = len(text_str)
    pattern_str_len = len(pattern_str)

    for i in range(text_str_len - pattern_str_len + 1):
        j = 0
        while j < pattern_str_len and pattern_str[j] == text_str[i + j]:
            j += 1
        if j == pattern_str_len:
            return i
    return -1


def find_all_occurrence_of_substring_brute_force(text_str, pattern_str):
    text_str_len = len(text_str)
    pattern_str_len = len(pattern_str)
    index_list = []
    for i in range(text_str_len - pattern_str_len + 1):
        j = 0
        while j < pattern_str_len and pattern_str[j] == text_str[i + j]:
            j += 1
        if j == pattern_str_len:
            index_list.append(i)
    return index_list


print(find_first_occurrence_of_substring_brute_force(
    "this is my first attempt for competitive coding. I don't have passion for coding.", "for"))
print(find_all_occurrence_of_substring_brute_force(
    "this is my first attempt for competitive coding. I don't have passion for coding.", "for"))
