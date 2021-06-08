"""
We have a staircase and we can move one step or two step at a time

What are the possible ways in which you can reach nth step

ways of reaching n = (ways of reaching n-1) + ways of reaching n-2

NOTE: it is fibonacci for 1 and 2 steps
But if we say we need to go up by 1 or 2 or 3 steps then it will be a fibonacci of sum of previous three numbers

"""


def reach_nth_step(n):
    if n in [0, 1]:
        return 1
    return reach_nth_step(n - 2) + reach_nth_step(n - 1)


print(reach_nth_step(6))
