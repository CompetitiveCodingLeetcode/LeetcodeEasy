"""

Given a list of contacts containing name and phone number , we need to group the contacts which either have the same name or same phone number together.

Example:
Input :{{abc ,9987},{xyz,9986},{dfg,9987}}
Output:{{{abc ,9987},{abc ,9987}},{{xyz,9986}}}

Union Find Algorithm or Depth First search Algorithm was applicable

"""


def group_contacts(input_list):
    input_list_len = len(input_list)
    same_group_list,ans_list = [], []
    for i in range(input_list_len-1):
        for j in range(i+1,input_list_len):
            if input_list[i][0] == input_list[j][0]:
                same_group_list.append(input_list[i])
                same_group_list.append(input_list[j])
            elif input_list[i][1] == input_list[j][1]:
                same_group_list.append(input_list[i])
                same_group_list.append(input_list[j])
        if same_group_list:
            ans_list.append(same_group_list)
        else:
            ans_list.append([input_list[i]])
        same_group_list = []
    return ans_list


print(group_contacts([('abc', 9987), ('xyz', 9986), ('dfg', 9987)]))
