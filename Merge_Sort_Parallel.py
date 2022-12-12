import math
import multiprocessing
import random
import sys
import time
from Get_name_list import name_list

letter_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def merge(*args):
    # Support explicit left/right args, as well as a two-item
    # tuple which works more cleanly with multiprocessing.
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:

        letter_index = 0
        while letter_list.index(left[left_index][letter_index].lower()) == letter_list.index(right[right_index][letter_index].lower()):
#            print(left[left_index], left[left_index][letter_index], right[right_index], right[right_index][letter_index], "Letter_index + 1", letter_index)
            letter_index = letter_index + 1

            if letter_index == len(left[left_index])-1:
                merged.append(left[left_index])
                left_index += 1
                letter_index = 0
#                print("////", left[left_index], left[left_index][letter_index], right[right_index], right[right_index][letter_index], "Letter_index + 1", letter_index)
                if left_index >= left_length:
                    break
            if letter_index == len(right[right_index])-1:
                merged.append(right[right_index])
                right_index += 1
                letter_index = 0
                if right_index >= right_length:
                    break

        if left_index >= left_length or right_index >= right_length:
            break
#        print(left[left_index], "//", right[right_index], letter_index)

        if letter_list.index(left[left_index][letter_index].lower()) < letter_list.index(right[right_index][letter_index].lower()):
            merged.append(left[left_index])
            left_index += 1
            letter_index = 0
#            print(left_index, "////", right_index, letter_index)

        if left_index >= left_length or right_index >= right_length:
            break

#        print(left[left_index], len(left[left_index]), "///", right[right_index], len(right[right_index]), right_length, letter_index)

        if letter_list.index(left[left_index][letter_index].lower()) > letter_list.index(right[right_index][letter_index].lower()):
            merged.append(right[right_index])
            right_index += 1
#            letter_index = 0
#            break


    if left_index == left_length:
        merged.extend(right[right_index:])

    else:
        merged.extend(left[left_index:])

#    print("merged", merged)
    return merged


def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = length // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def merge_sort_parallel(data):
    # Creates a pool of worker processes, one per CPU core.
    # We then split the initial data into partitions, sized
    # equally per worker, and perform a regular merge sort
    # across each partition.
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(data)) / processes))
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(merge_sort, data)
    # Each partition is now sorted - we now just merge pairs of these
    # together using the worker pool, until the partitions are reduced
    # down to a single sorted result.
    while len(data) > 1:
        # If the number of partitions remaining is odd, we pop off the
        # last one and append it back after one iteration of this loop,
        # since we're only interested in pairs of partitions to merge.
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]


# if __name__ == "__main__":
#   size = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 1000
#    data_unsorted = ["cvsdvds", "dssa", "dssa", "asdasd", "wbasd", "edfgasd"]
#    data_unsorted = ["c", "d", "e", "a", "f", "g", "h"]
#    data_unsorted = name_list
#    data_sorted = merge_sort_parallel(data_unsorted)
#    print(merge_sort_parallel(data_unsorted))
