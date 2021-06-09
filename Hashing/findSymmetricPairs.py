"""
Given a list of number pairs
If pair(i,j) exist and pair(j,i) exist report all such pairs

"""


def find_symmetric_pairs(input_list):
    pair_map = {}
    answer_list = []
    input_list_len = len(input_list)
    for i in range(0, input_list_len):
        if input_list[i][1] in pair_map and pair_map[input_list[i][1]] == input_list[i][0]:
            answer_list.append(input_list[i])
            answer_list.append((input_list[i][1], input_list[i][0]))
        else:
            pair_map[input_list[i][0]] = input_list[i][1]
    return answer_list


print(find_symmetric_pairs([(1, 2), (3, 4), (5, 6), (2, 1), (6, 5)]))
