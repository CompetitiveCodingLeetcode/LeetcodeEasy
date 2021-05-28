import time


def LinearSearch(nums: list, value: int) -> int:
    start = time.time()

    for num in nums:
        if num == value:
            return nums.index(value)

    # enumerate approach
    # for idx, num in enumerate(nums):
    #     if num == value:
    #         pos = idx
    #         break
    end = time.time()
    print("time taken =", end - start)
    # time taken = 3.5762786865234375e-06 for index() approach
    # time taken = 5.9604644775390625e-06 for enumerate() approach
    return -1


print(LinearSearch([2, 4, 6, 8, 5], 5))
