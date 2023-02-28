import numpy as np


def main():
    _ = int(input())
    nums = list( map( np.int64, input().split() ) )
    # The map() function applies a function (casting to int) over entries in an iterable (the list)

    print( max_pair_prod(nums) )
    #print(100000 * 90000)


def max_pair_prod(nums):
    n = len(nums)

    max_1_index = 0
    for i in range(0, n):
        if nums[i] > nums[max_1_index]:
            max_1_index = i

    max_2_index = max_1_index - 1
    for i in range(0, n):
        if ( (i != max_1_index) and (nums[i] > nums[max_2_index]) ):
            max_2_index = i

    result = np.int64(nums[max_1_index]) * np.int64(nums[max_2_index])

    return np.int64(result)


if __name__ == '__main__':
    main()
