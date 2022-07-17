def find_sum(i):
    num = i
    digit_sum = 0
    while num != 0:
        d = num % 10
        digit_sum += d
        num = num // 10

    digit_sum = (digit_sum*2) + 1
    return digit_sum



def solve(S):
    if S==1:
        return 1
    else:
        sum = 0
        i = 2
        while S < 100000 and sum!=S:
            sum = find_sum(i)
            i += 2

        if sum == S:
            return i-2
        else:
            return -1


print(solve(9))
print(solve(15))