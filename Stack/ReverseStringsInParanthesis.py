"""
reverse strings in parantheses and the output should not contain parantheses
Input: ((ng)ipm(ca))
output: camping

"""

def reverse_strings_in_parentheses(input_str):
    stack_str = []
    input_str_len = len(input_str)
    for i in range(input_str_len):
        if input_str[i] == '(':
            stack_str.append(i)
        elif input_str[i] == ')':
            temp_idx = stack_str.pop()
            rev_temp = input_str[i-1:temp_idx:-1]
            input_str = input_str[:temp_idx+1] + rev_temp + input_str[i:]

    result = ""
    for ch in input_str:
        if ch != '(' and ch != ')':
            result += ch

    return result

print(reverse_strings_in_parentheses("((ng)ipm(ca))"))
print(reverse_strings_in_parentheses("ab(cd)"))
print(reverse_strings_in_parentheses("(geeks(for)geeks)"))