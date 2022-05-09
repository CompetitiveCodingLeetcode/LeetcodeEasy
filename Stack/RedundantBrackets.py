"""
Given a string of balanced expression, find if it contains a redundant parenthesis or not. A set of parenthesis are redundant if the same sub-expression is surrounded by unnecessary or multiple brackets. Print ‘Yes’ if redundant, else ‘No’.
Note: Expression may contain ‘+‘, ‘*‘, ‘–‘ and ‘/‘ operators. Given expression is valid and there are no white spaces present.

Example:


Input:
((a+b))
(a+(b)/c)
(a+b*(c-d))
Output:
Yes
Yes
No

Explanation:
1. ((a+b)) can reduced to (a+b), this Redundant
2. (a+(b)/c) can reduced to (a+b/c) because b is
surrounded by () which is redundant.
3. (a+b*(c-d)) doesn't have any redundant or multiple
brackets.

"""

# time complexity: O(n)
def has_redundant_brackets(s:str):
    operators = ['+','-','*','/']
    stack=[]
    for ch in s:
        #if ch is ( or ay operator then push in stack
        if ch == '(' or ch in operators:
            stack.append(ch)
        else:
            # it means there is ) bracket definitely present corresponding to the opening bracket
            if ch == ')':
                # there are two cases possible: for a pair of brackets there will be an operator present and hence no redundancy else redundancy
                is_redundant = True
                while stack[-1] != '(':
                    c = stack.pop()
                    if c in operators:
                        is_redundant = False

                if is_redundant == True:
                    return True
                # to pop the opening bracket in stack
                stack.pop()
    return False

print(has_redundant_brackets("((a+b))"))
print(has_redundant_brackets("(a+(b)/c)"))
s="(a+b*(c-d))"
print(has_redundant_brackets(s))






